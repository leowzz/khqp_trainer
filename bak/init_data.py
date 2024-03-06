#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pydantic import BaseModel


class BatchDataBase(BaseModel):
    year: int | None = None
    census_batch: str | None = None  # 普查批次
    id_code: str | None = None  # 编号
    precision: str | None = None  # 精度
    is_train: bool | None = None
    is_validation: bool | None = None

    ann_file: str | None = None
    img_prefix: str | None = None
    filter_empty_gt: bool | None = None
    update_cache: bool | None = None


class BatchDataRead(BatchDataBase):
    id: int

    class Config:
        orm_mode = True


