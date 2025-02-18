#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime

from pydantic import BaseModel


class BatchDataBase(BaseModel):
    year: int | None = None
    census_batch: str | None = None  # 普查批次
    id_code: str | None = None  # 编号
    precision: str | None = None  # 精度
    is_train: bool | None = None
    is_validation: bool | None = None

    ann_file: str | None = None
    ann_file_lbs: str | None = None
    img_prefix: str | None = None
    filter_empty_gt: bool | None = None
    update_cache: bool | None = None
    create_at: datetime | None = None


class BatchDataRead(BatchDataBase):
    id: int

    class Config:
        orm_mode = True


class BatchDataCreate(BatchDataBase):
    year: int | None = 2024
    census_batch: str | None = ''  # 普查批次
    id_code: str | None = ''  # 编号
    precision: str | None = ''  # 精度
    is_train: bool | None = True
    is_validation: bool | None = False

    ann_file: str | None = ''
    ann_file_lbs: str | None = ''
    img_prefix: str | None = ''
    filter_empty_gt: bool | None = False
    update_cache: bool | None = False
    create_at: datetime | None = datetime.now()
