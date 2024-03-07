#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from loguru import logger

from bak.evolve_config2 import train_data, val_data
from bak.init_data import BatchDataBase, BatchDataRead
from db_utils import BatchData, session

logger.debug(f"{len(val_data)=}")
for td in val_data:
    db_obj = BatchData(**BatchDataBase(**td).dict())
    batch_data_db = session.query(BatchData).where(BatchData.img_prefix == td.get("img_prefix")).first()
    if batch_data_db:
        logger.debug(f"{BatchDataRead.from_orm(batch_data_db)=}")
        continue
    session.add(db_obj)

#     if '2023' in db_obj.ann_file:
#         batch_data_db.year = 2023
#     census_batch_idx = db_obj.ann_file.index('kh')
#     if census_batch_idx:
#         census_batch = db_obj.ann_file[census_batch_idx:census_batch_idx + 4].upper()
#         census_batches.append(census_batch)
#         batch_data_db.census_batch = census_batch
#
#     batch_data_db.precision = 'S3'
#     batch_data_db.is_train = True
#     batch_data_db.is_validation = False
#
#     id_code_idx = census_batch_idx + 5
#     if batch_data_db.id_code is None:
#         if batch_data_db.id > 29:
#             code_start = db_obj.ann_file[id_code_idx + 21:]
#             code_end = code_start.index('_')
#             id_code = db_obj.ann_file[id_code_idx + 21:][:code_end]
#             logger.debug(f"{id_code}, {db_obj.ann_file[id_code_idx + 21:]}, {db_obj.ann_file[id_code_idx:]}, {batch_data_db.id=}")
#             batch_data_db.id_code = id_code

        # if batch_data_db.id > 25 and batch_data_db.id <= 29:
        #     code_start = db_obj.ann_file[id_code_idx + 18:]
        #     code_end = code_start.index('_')
        #     id_code = db_obj.ann_file[id_code_idx + 18:][:code_end]
        #     logger.debug(f"{db_obj.ann_file[id_code_idx + 18:]}, {db_obj.ann_file[id_code_idx:]}, {id_code}, {batch_data_db.id=}")
        #     batch_data_db.id_code = id_code
        # if 2 < batch_data_db.id <= 25:
        #     id_code = db_obj.ann_file[id_code_idx:id_code_idx + 3]
        #     logger.debug(f"{id_code=}")
        #     batch_data_db.id_code = id_code

        # if 25 < batch_data_db.id <= 25:
        #     id_code = db_obj.ann_file[id_code_idx:id_code_idx + 3]
        #     logger.debug(f"{id_code=}")
        #     batch_data_db.id_code = id_code

    # if not batch_data_db:
    #     logger.debug(f"insert {db_obj.ann_file=}")
    #     session.add(db_obj)

session.commit()

