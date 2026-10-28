from aiogram import  Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext 
from service import *




router = Router()







@router.message(Command("start"))
async def start_bot(message: Message):
        await message.answer(f"Hello @{message.from_user.username}")
        # , reply_markup=main_kb

@router.message(Command("help"))
async def help_bot(message : Message):
        await message.answer("""
привет ето библиотека ну ты програмист далше сам поймеш
""")






class Create_book(StatesGroup):
    get_title = State()
    get_caption = State()
    get_publisher = State()
    get_author_id = State()
    get_category_id = State()





class  Update_book(StatesGroup):
    get_title = State()
    get_caption = State()
    get_publisher = State()
    get_book_id = State()




class create_author(StatesGroup):
      get_name = State()
      get_age = State()



class create_category(StatesGroup):
      get_category_name= State()

class delete_book_for_me(StatesGroup):
     get_book_id = State()




class seek_book_by_id(StatesGroup):
     get_book_id = State()


    



@router.message(Command("create_book"))
async def create_book(message : Message, state : FSMContext):
    await message.answer("Введите свой title: ")
    await state.set_state(Create_book.get_title)



@router.message(Create_book.get_title)
async def get_title(message : Message, state : FSMContext):
      await state.update_data(title = message.text)
      await message.answer("Введите свой caption: ")
      await state.set_state(Create_book.get_caption)




@router.message(Create_book.get_caption)
async def get_caption(message : Message, state : FSMContext):
      await state.update_data(caption = message.text)
      await message.answer("Введите свой publisher: ")
      await state.set_state(Create_book.get_publisher)





@router.message(Create_book.get_publisher)
async def get_publisher(message : Message, state : FSMContext):
      await state.update_data(publisher = message.text)
      await message.answer("Введите свой author_id: ")
      await state.set_state(Create_book.get_author_id)




@router.message(Create_book.get_author_id)
async def get_author_id(message : Message, state : FSMContext):
    await state.update_data(author_id = int(message.text))
    await message.answer("Введите свой category_id: ")
    await state.set_state(Create_book.get_category_id)


@router.message(Create_book.get_category_id)
async def get_category_id(message : Message, state : FSMContext):
    await state.update_data(category_id = int(message.text))
    data = await state.get_data()
    await create_book_for_me(data["title"], data["caption"], data["publisher"], data["author_id"], data["category_id"])
    await message.answer("Книга создана успешно!!!")
    await state.clear()

    
@router.message(Command("add_author"))
async def add_auth(message : Message , state : FSMContext):
      await message.answer("Введите имя автора")
      await state.set_state(create_author.get_name)


@router.message(create_author.get_name)
async def cre_name(message : Message , state : FSMContext):
      await state.update_data(name = message.text)
      await message.answer('Введите возраст автора: ')
      await state.set_state(create_author.get_age)



    
@router.message(create_author.get_age)
async def cre_age(message : Message , state : FSMContext):
    await state.update_data(age = int(message.text))
    data = await state.get_data()
    await create_author(data["name"], data["age"])
    await message.answer("Автор создан!!!")
    await state.clear()





@router.message(Command("add_category"))
async def add_cat(message : Message , state : FSMContext):
      await message.answer("Введите свою категорию")
      await state.set_state(create_category.get_category_name)




@router.message(create_category.get_category_name)
async def get_cat_name(message : Message , state : FSMContext):
    await state.update_data(name = message.text)
    data = await state.get_data()
    await create_category_for_me(data["name"])
    await message.answer("категория создана!!!")
    await state.clear()























@router.message(Command("update_book"))
async def a1(message : Message, state : FSMContext):
    await message.answer("Введите свой title: ")
    await state.set_state(Update_book.get_title)



@router.message(Update_book.get_title)
async def a2(message : Message, state : FSMContext):
      await state.update_data(title = message.text)
      await message.answer("Введите свой caption: ")
      await state.set_state(Update_book.get_caption)




@router.message(Update_book.get_caption)
async def a3(message : Message, state : FSMContext):
      await state.update_data(caption = message.text)
      await message.answer("Введите свой publisher: ")
      await state.set_state(Update_book.get_publisher)





@router.message(Update_book.get_publisher)
async def a4(message : Message, state : FSMContext):
      await state.update_data(publisher = message.text)
      await message.answer("Введите свой book_id: ")
      await state.set_state(Update_book.get_book_id)


@router.message(Update_book.get_book_id)
async def a5(message : Message, state : FSMContext):
    await state.update_data(book_id = int(message.text))
    data = await state.get_data()
    await update_book_for_me(data["title"], data["caption"], data["publisher"], data["book_id"])
    await message.answer("Книга успешно обновлена!!!")
    await state.clear()















@router.message(Command("delete_book"))
async def delete_book_my(message : Message , state : FSMContext):
     await message.answer("Введите id книги которой хотите удалит!!!!")
     await state.set_state(delete_book_for_me.get_book_id)



@router.message(delete_book_for_me.get_book_id)
async def emnvjk3rnbvetnbu4t(message : Message , state : FSMContext):
     await state.update_data(book_id = int(message.text))
     data = await state.get_data()
     await delete_book(data["book_id"])
     await message.answer("Ваша книга удалена!!!!")
     await state.clear()













@router.message(Command("seek_book_with_id"))
async def cmkvmkpvmefvm(message : Message , state : FSMContext):
     await message.answer("Введите id таска которого хотите найти")
     await state.set_state(seek_book_by_id.get_book_id)


@router.message(seek_book_by_id.get_book_id)
async def rifjrjvnj(message : Message , state : FSMContext):
     await state.update_data(book_id = int(message.text))
     data = await state.get_data()

     a = await seek_book(data["book_id"])
     if not a:
       await message.answer("Книга не найдена")
     result = ""
     for i in a:
          result += f"""
===== Id{i["id"]} =====
Title: {i["title"]}
Caption: {i["caption"]}
publisher: {i["publisher"]}
category_id: {i["category_id"]}
author_id: {i["author_id"]}
"""
     await message.answer(result)
     await state.clear()






@router.message(Command("all_books"))
async def show_all_books(message : Message):
    a = await get_all_books()
    if not a:
        await message.answer("Книги не найдены")
    result = ""
    for i in a:
        result += f"""
===== Id{i["id"]} =====
Title: {i["title"]}
Caption: {i["caption"]}
publisher: {i["publisher"]}
author_id: {i["author_id"]}
category_id: {i["category_id"]}
"""
    await message.answer(result)


class Seek_books_by_author(StatesGroup):
    get_author_id = State()


@router.message(Command("seek_book_by_author"))
async def ask_author_id(message : Message, state : FSMContext):
    await message.answer("Введите author_id:")
    await state.set_state(Seek_books_by_author.get_author_id)


@router.message(Seek_books_by_author.get_author_id)
async def show_books_by_author(message : Message, state : FSMContext):
    await state.update_data(author_id = int(message.text))
    data = await state.get_data()
    a = await seek_books_by_author(data["author_id"])
    if not a:
        await message.answer("Книги нету")
    result = ""
    for i in a:
        result += f"""
===== Id{i["id"]} =====
Title: {i["title"]}
Caption: {i["caption"]}
publisher: {i["publisher"]}
author_id: {i["author_id"]}
category_id: {i["category_id"]}
"""
    await state.clear()

    await message.answer(result)


class Seek_books_by_category(StatesGroup):
    get_category_id = State()


@router.message(Command("seek_book_by_category"))
async def ask_category_id(message : Message, state : FSMContext):
    await message.answer("Введите category_id:")
    await state.set_state(Seek_books_by_category.get_category_id)


@router.message(Seek_books_by_category.get_category_id)
async def show_books_by_category(message : Message, state : FSMContext):
    await state.update_data(category_id = int(message.text))
    data = await state.get_data()
    a = await seek_books_by_category(data["category_id"])
    await state.clear()
    if not a:
        await message.answer("Книги нету")
    result = ""
    for i in a:
        result += f"""
===== Id{i["id"]} =====
Title: {i["title"]}
Caption: {i["caption"]}
publisher: {i["publisher"]}
author_id: {i["author_id"]}
category_id: {i["category_id"]}
"""
    await message.answer(result)
