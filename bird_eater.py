from birdy.twitter import UserClient
import ast
import json
import pprint

client = UserClient(Consumer_key, Consumer_secret,
                    Access_Token, Access_Token_secret)

posts = client.api.users.show.get(screen_name='eEuler_eSec')
#json_data = ast.literal_eval(str(posts.data))
pprint.pprint(json.dumps(posts.data))
