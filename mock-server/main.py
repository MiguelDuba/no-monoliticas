import asyncio
import tornado
from companies.handler import *
from cadastral.handler import *



def make_app():
    return tornado.web.Application([
        (r"/companies", CompanyHandler),
        (r"/cadastral", CadastralHandler)
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    print("Mock server starting ...")
    asyncio.run(main())