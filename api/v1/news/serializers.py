from rest_framework import serializers
from news.models import News,Category,Comment


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # news = NewsSerializer(many = True)  
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text"]































# class NewsSerializer(serializers.ModelSerializer):
#     time_since_publication = serializers.SerializerMethodField()

#     class Meta:
#         model = models.News
#         exclude = ('id',)

#     def get_time_since_publication(self, object):
#         publication_date = object.publication_date
#         now = datetime.now()
#         time_delta = timesince(publication_date, now)
#         return time_delta

#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and description must different")
#         return data
    
#     def validate_title(self, value):
#         if len(value) < 10:
#             raise serializers.ValidationError("The title must be at least 10 character")
#         return value


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = "__all__"