from pull_posts import get_posts_from_repo
from Post import Post
from firebase import firebase
posts = get_posts_from_repo('mihirk/posts')
posts = map(lambda post: Post(post).json(), posts)


firebase_handle = firebase.FirebaseApplication('https://notdecidedblog.firebaseio.com', None)
firebase_handle.post('/posts',posts[0])
