from django.db import models

# Create your models here.



class Grades(models.Model):

    g_name = models.CharField(max_length=20)
    g_date = models.DateTimeField()
    g_girl_num = models.IntegerField()
    g_boy_num = models.IntegerField()
    isDelete = models.BooleanField(default=False)


    def __str__(self):
        return self.g_name
    class Meta:
        db_table = "grades"  # 表名
        ordering = ['id']


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    def createStudent(self, name, age, gender, contend, grade, isD):
        stu2 = self.models()
        stu2.s_name = name
        stu2.s_age = age
        stu2.s_gender = gender
        stu2.s_contend = contend
        stu2.grades = grade
        stu2.isDelete = isD





class Students(models.Model):

    # 定义一个类方法
    @classmethod
    def createStudent(cls, name, age, gender, contend, grade, isD):
        stu = cls(s_name=name, s_age=age, s_contend=contend, s_gender=gender, grades=grade, isDelete=isD)
        return stu

    # 自定义管理器
    # stuObj = models.Manager()
    stuObj = StudentManager()
    s_name = models.CharField(max_length=20)
    s_gender = models.BooleanField(default=True)
    s_age = models.IntegerField()
    s_contend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    grades = models.ForeignKey(Grades, on_delete=models.CASCADE)
    # 这里有不同 on_delete 与其他版本不同


    def __str__(self):

        return self.s_name


    class Meta:
        db_table = "students"  # 表名
        ordering = ['id']





