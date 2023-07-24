from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

# Configure redis caching
app.config['CACHE_TYPE'] = 'RedisCache'  
app.config['CACHE_REDIS_HOST'] = 'redis'
app.config['CACHE_DEFAULT_TIMEOUT'] = 60 * 60 # 1 hour

cache = Cache(app)

@app.route('/posts')
@cache.cached()
def get_posts():
  # expensive db query
  posts = Post.query.all()
  return jsonify(posts)


@cache.cached(timeout=60)
def get_user(user_id):
  # db lookup
  return User.query.get(user_id)