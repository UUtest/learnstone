from sqlalchemy import Column, String, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类：
Base = declarative_base()

#定义User对象：
class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    #多的一方的book是通过外健关联到user表的
    usr_id = Column(String(20), ForeignKey('user.id'))
class User(Base):
    #table的名字
    __tablename__ = 'user'

    #表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    #一对多：
    books = relationship('Book')

#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
#创建DBSession类型：
DBSession = sessionmaker(bind=engine)

# #创建增加session
# session = DBSession()
# #创建新User对象
# new_book = Book(id = '1', name = 'Mobook', user_id='5')
# #添加到session:
# session.add(new_book)
# #提交即保存到数据库
# session.commit()
# #关闭session
# session.close()

#创建查询session
session = DBSession()
#创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行：
user = session.query(User).filter(User.id=='5').one()
#打印类型和对象的name属性
print('type:', type(user))
print('type:', user.name)
#关闭session
session.close()