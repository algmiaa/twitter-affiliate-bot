import tweepy
import random
import time

# مفاتيح Twitter API – استبدلها بمفاتيحك الخاصة
api_key = "41RpFvHyS9dV2XqoyZGnIl2oW"
api_secret = "QsSj478XGqACZq2hbbmOXVEMqLHiWNiJio1Kv6Wph98izP2O5P"
access_token = "1471975876187332610-iXIgitaOrBgSPyuFcZpCKaCXYlAGeT"
access_token_secret = "2q5GKGMOxNLmr8GVuB5EaTrEbywxau9UiB7H10KFENb7M"

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

tweets = [
    "🎧 سماعات رائعة بسعر ممتاز: https://s.click.aliexpress.com/e/_example1",
    "📱 حامل مغناطيسي للهاتف: https://s.click.aliexpress.com/e/_example2",
    "🧼 جهاز تنظيف الوجه الأكثر مبيعًا: https://s.click.aliexpress.com/e/_example3"
]

while True:
    tweet = random.choice(tweets)
    try:
        api.update_status(tweet)
        print("✅ تم نشر التغريدة:", tweet)
    except Exception as e:
        print("❌ خطأ:", e)
    time.sleep(3600)  # تغريدة كل ساعة
