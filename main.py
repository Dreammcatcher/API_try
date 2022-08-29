import pony
import bit
import fastapi

api = fastapi.FastAPI()

@api.get('/hello')
def api_hello():
    return {'hello': 'from apiii'}


def main():
    pass


# if __name__ == '__main__':
#     main()


