# Generated by Django 2.2.6 on 2019-11-01 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ammanarul', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('prayer', models.CharField(choices=[('(Student) Almighty Nalla Mark Amma, please help me get good marks in my exams.', '(Student) Almighty Nalla Mark Amma. Please help me get good marks in my exams.'), ('(Jobseeker) Almighty Nalla Mark Amma, please help me get a good job.', '(Jobseeker) Almighty Nalla Mark Amma, please help me get a good job.'), ('(Employed) Almighty Nalla Mark Amma, please help me get get the promotion that I am looking forward to.', '(Employed) Almighty Nalla Mark Amma, please help me get get the promotion that I am looking forward to.'), ('(Parent) Almighty Nalla Mark Amma, please help my child.', '(Parent) Almighty Nalla Mark Amma, please help my child.'), ('(Marriage Help) Almighty Nalla Mark Amma, please help me to get married.', '(Marriage Help) Almighty Nalla Mark Amma, please help me to get married.'), ('(Family Problems) Almighty Nalla Mark Amma, please solve my family problems.', '(Family Problems) Almighty Nalla Mark Amma, please solve my family problems.')], default='(Student) Almighty Nalla Mark Amma, please help me get good marks in my exams.', max_length=200)),
                ('created', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Premium',
        ),
    ]