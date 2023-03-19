### url
* 在第一层urls.py中设置子路由

```
urlpatterns = [
    path('', include('myglory.urls'))
]
```

* 对应myglory文件夹下的urls.py

```
# GloryHeroList 是APIView 记得引入
urlpatterns = [
    path('gloryherolist/', GloryHeroList.as_view()),
]
```

### views.py

```
class GloryHeroList(APIView):
	def get(self, request):
		...  # 这里用到model和serializers
	def post(self, request):
		...
```

### models.py

```
class GloryHero(models.Model):
	... 各种属性 
	# 比如
	name = models.CharField(max_length=20)
```

### serializers.py

```
class GloryHeroSerializer(serializers.Serializer):
	... 序列化的属性
	# 比如
	name = serializers.CharField(max_length=20)
	
	# 添加
	def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return GloryHero.objects.create(**validated_data)
	
	# 预计还有修改和删除
	
	# 然后
	class Meta:
        model = GloryHero
        fields = ('name', 'proficiency', 'proficiency_level', 'image', 'speciality', 'strong_period', 'live_ability', 'damage_ability', 'difficulty', 'passive_skill', 'skill_1', 'skill_2', 'skill_3')
```

