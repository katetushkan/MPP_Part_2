import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from manager.models import ManagerTask
from django_graphene_permissions.permissions import AllowAny


class TaskType(DjangoObjectType):
    class Meta:
        model = ManagerTask


class Query(ObjectType):
    task = graphene.Field(TaskType, id=graphene.Int())
    tasks = graphene.List(TaskType)

    def resolve_task(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ManagerTask.objects.get(pk=id)
        return None

    def resolve_tasks(self, info, **kwargs):
        return ManagerTask.objects.all()


class TaskInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    status = graphene.String()
    deadline = graphene.Date()
    description = graphene.String()


class CreateTask(graphene.Mutation):
    class Arguments:
        input = TaskInput(required=True)
    ok = graphene.Boolean()
    task = graphene.Field(TaskType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        task_instance = ManagerTask(name=input.name, status=input.status, deadline=input.deadline, description=input.description)
        task_instance.save()

        return CreateTask(ok=ok, task=task_instance)


class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TaskInput(required=True)
    ok = graphene.Boolean()
    task = graphene.Field(TaskType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        task_instance = ManagerTask.objects.get(pk=id)
        if task_instance:
            ok = True
            task_instance.name = input.name
            task_instance.status = input.status
            task_instance.deadline = input.deadline
            task_instance.description = input.description
            task_instance.save()
            return UpdateTask(ok=ok, task=task_instance)
        return UpdateTask(ok=ok, task=None)


class DeleteUser(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        task = ManagerTask.objects.get(pk=kwargs["id"])
        task.delete()
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)