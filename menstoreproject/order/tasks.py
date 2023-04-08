from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_order_info_email_task(email_address, message):
    send_mail(
        'ЗАМОВЛЕННЯ ПРИЙНЯТО',
        f"\t{message}\n\n",
        'sapalstanislav@ukr.net',
        [email_address],
        fail_silently=False,
    )
