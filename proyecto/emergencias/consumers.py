import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Estado
from core.models import UserSigemco
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync


class EmergenciasConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		await self.channel_layer.group_add("users", self.channel_name)
		print(f"Agregado el canal {self.channel_name} al canal users")
		user = self.scope['user']
		if user.is_authenticated:
			await self.update_user_status(user, True)
			await self.send_status()
			await self.usuario_en_linea()

	async def disconnect(self, code):
		await self.channel_layer.group_discard("users", self.channel_name)
		print(f'Removiendo {self.channel_name} channel from users')
		user = self.scope['user']
		if user.is_authenticated:
			await self.update_user_status(user, False)
			await self.send_status()

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

	async def send_status(self):
		users = UserSigemco.objects.all()
		logueados = 0
		for user1 in users:
			if user1.estado.status == True:
				logueados = logueados + 1
		html_users = render_to_string(
		    "modificar_estado_usuarios.html", {'users': users})
		await self.channel_layer.group_send(
			'users',
			{
				"type": "user_update",
				"event": "Change Status",
				"html_users": html_users,
				"dato": logueados
			}
		)

	async def user_update(self, event):
			await self.send_json(event)
			print('user_update', event)

	async def usuario_en_linea(self):
		users = UserSigemco.objects.all()
		logueados = 0
		for user1 in users:
			if user1.estado.status == True:
				logueados = logueados + 1
		await self.send_json(logueados)


	@database_sync_to_async
	def update_user_status(self, user,status):
		print(f"{user.username} cambió el estado")
		return Estado.objects.filter(user_id=user.pk).update(status=status)
