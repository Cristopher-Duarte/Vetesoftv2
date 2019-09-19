insert into Medicamento values(null, "CARDIOVET");
insert into Medicamento values(null, "MIRRAPEL");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");
insert into Medicamento values(null, "");


insert into ExamenMascota values(null, "SANGRE");
insert into ExamenMascota values(null, "RADIOGRAFIAS");
insert into ExamenMascota values(null, "ORINA");



from django.contrib.auth.models import User
c= User.objects.create_user("", "", "")
permiso= Permission.objects.get(name='Is Admin')
c.user_permissions.add(permiso)
c.save()