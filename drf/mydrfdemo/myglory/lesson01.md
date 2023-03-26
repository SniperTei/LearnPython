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

### 然后detail的url也配置上

```
urlpatterns = [
    path('gloryherolist/', GloryHeroList.as_view()),
    path('gloryherolist/<int:id>', GloryHeroDetail.as_view()),
]
```

### detail的view(改和删)

```
class GloryHeroDetail(APIView):
    
    def get(self, request, id):
        gloryheros = GloryHero.objects.get(id=id)
        serializer = GloryHeroSerializer(gloryheros)
        return Response(serializer.data)
    
    def put(self, request, id):
        print("put id: ", id)
        serializer = GloryHeroSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            # n = GloryHero.objects.get(id=id).update(**serializer.validated_data)
            n = GloryHero.objects.filter(id=id).update(**serializer.validated_data)
            print("n: ", n)
            gloryhero = GloryHero.objects.get(id=id)
            # 保存
            serializer = GloryHeroSerializer(gloryhero)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response(serializer.errors, status=200)
    
    def delete(self, request, id):
        gloryheros = GloryHero.objects.get(id=id)
        gloryheros.delete()
        return Response(status=200)
```


