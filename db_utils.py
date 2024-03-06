#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from loguru import logger
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from bak.evolve_config2 import train_data
from bak.init_data import BatchDataBase

Base = declarative_base()
# 创建 SQLite 数据库引擎
engine = create_engine('sqlite:///data.db', echo=False)


class BatchData(Base):
    __tablename__ = 'batch_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    census_batch = Column(String)  # 普查批次
    id_code = Column(String)
    precision = Column(String)  # 精度
    is_train = Column(Integer)
    is_validation = Column(Integer)
    ann_file = Column(String)
    img_prefix = Column(String)
    filter_empty_gt = Column(Integer)
    update_cache = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine, )
session = Session()