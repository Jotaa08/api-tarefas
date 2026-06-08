from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    prioridade = models.CharField("Prioridade", max_length=50)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField("Data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.titulo