from app import *
from app import mongo
from bson.json_util import ObjectId


class Article():


    def addArticle(self, blog):
        resp = mongo.db.articles.insert_one(blog)

        return resp

    def getAllArticles(self):
        articles = mongo.db.articles.find()

        return articles

    def deleteAnArticle(self, id):
        resp = mongo.db.articles.delete_one({'_id':ObjectId(id)})

        return resp

    def getAnArticle(self, id):
        resp = mongo.db.articles.find_one({'_id': ObjectId(id)})

        return resp

    def addComment(self, comment):
        resp = mongo.db.comments.insert_one(comment)

        return resp

    def getAllComments(self):
        comments = mongo.db.comments.find()

        return comments

    def updateAnArticle(self, id, updated_blog):
        updated = {
            'title': updated_blog['title'],
            'domain': updated_blog['domain'],
            'body': updated_blog['body']
        }
        article = mongo.db.articles.update_one({'_id':ObjectId(id)}, {'$set':updated})

        return article

    def addLikes(self, username, likes):
        resp = mongo.db.articles.update_one({'author': username},{'$set':{'likes':likes}})

        return resp

    def getUserArticles(self, username, email):
        resp = mongo.db.articles.find({'author': username})

        return resp

    def getMostRecent(self):
        resp = mongo.db.articles.find({'title': 1, 'body': 1, 'author': 1, 'datetime': 1, 'likes': 1}).sort({'likes': -1})

        return list(resp)