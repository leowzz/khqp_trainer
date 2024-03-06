update_cache = False
train_data = [
    # khdp_7flys
    dict(
        img_prefix='/data/data/split_ss_yimu_m6_p2/train_khdp_7flys_gsd5_orgsize_noDecay_seg-v2/images',
        ann_file='/data/data/split_ss_yimu_m6_p2/train_khdp_7flys_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230531_p1p2',
        select_ids=None,
        filter_empty_gt=False,
        update_cache=False,
    ),
    # khdp_v2_3flys
    dict(
        img_prefix='/data/data/split_ss_yimu_m6_p1/train_khdp_v2_3flys_gsd5_orgsize_noDecay_seg-v2/images',
        ann_file='/data/data/split_ss_yimu_m6_p1/train_khdp_v2_3flys_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230531_p1p2',
        select_ids=None,
        filter_empty_gt=False,
        update_cache=update_cache,
    ),
    # khdp_v3
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_044_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_044_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_064_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_064_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_065_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_065_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_073_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_073_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_072_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_072_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    # khdp_v4
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_013_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_013_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_015_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_015_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_016_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_016_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_028_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_028_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    # khdp_202306_zhubin
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_067_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_067_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_068_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_068_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_069_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_069_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_070_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_070_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_071_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_071_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_075_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_075_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_078_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_078_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_080_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_080_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_081_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_081_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_082_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_082_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_084_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_084_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_087_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_087_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_089_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_089_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_090_mod_loc_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_202306016',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_090_mod_loc_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False, 'update_cache': update_cache},

    # KHXP_DZ
    {
        'ann_file': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_001a002_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_001a002_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_003a004a006_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_003a004a006_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_005_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_005_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_007a008_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khxpdz/patch_2023_khdz_007a008_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    ################### khqp 2023 ###################
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_001a006a010_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_001a006a010_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_002a004_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_002a004_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_003_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_003_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_005_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_005_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_007a008a009_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_007a008a009_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_011_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_011_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_012a013_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_012a013_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_014a038_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_014a038_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_015a016_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_015a016_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_018a069_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_018a069_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_019a075_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_019a075_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_020a022_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_020a022_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_023a025_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_023a025_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_026a029a079_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_026a029a079_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_028a027a030_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_028a027a030_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_032a033_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_032a033_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_039a040_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_039a040_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_042a045_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_042a045_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_046a049_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_046a049_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_050a058_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_050a058_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_053a059a060_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_053a059a060_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_054a056_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_054a056_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_063a143_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_063a143_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_073a074a080_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_073a074a080_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_072a081a082_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_072a081a082_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_076_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_076_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_077a078_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_077a078_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_091a097a102a104_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_091a097a102a104_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_087a088a089a090_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_087a088a089a090_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_094_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_094_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    # unqualified data
    # {
    #    'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_031a101_gsd5_s2048/annfiles',
    #    'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_031a101_gsd5_s2048/images',
    #    'filter_empty_gt': False,
    #    'update_cache': update_cache
    # },

    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_105a0111_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_105a0111_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_112a113_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_112a113_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_114a116a118_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_114a116a118_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_115_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_115_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_117_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_117_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_119a120_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_119a120_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_034a131_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_034a131_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_132a133_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_132a133_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_057_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_057_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_066a142_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_066a142_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_106a107a138a139_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_106a107a138a139_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    }

]

val_data = [
    ### test_and_val ###
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_059_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230531',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_059_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False,
        'update_cache': update_cache,
    },
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_039A_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230531',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_039A_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False,
        'update_cache': update_cache,
    },
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_039B_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230531',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_039B_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False,
        'update_cache': update_cache,
    },
    {
        'ann_file': '/data/data/split_ss_yimu_m6_p4/test_khdp_007_gsd5_orgsize_noDecay_seg-v2/annfiles2_labelme_20230601',
        'img_prefix': '/data/data/split_ss_yimu_m6_p4/test_khdp_007_gsd5_orgsize_noDecay_seg-v2/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },

    # khqp 2023
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_095a096a103_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_095a096a103_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_119a120_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_119a120_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
    {
        'ann_file': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_122_gsd5_s2048/annfiles',
        'img_prefix': '/data/data/split_ss_yimu_khqp_2023/patch_2023_khqp_122_gsd5_s2048/images',
        'filter_empty_gt': False,
        'update_cache': update_cache
    },
]

evolve_r = 0.02

ckpt_path = '/data/output/yolox_swinT_small_ds8x_s2048_s3_experiment42/backup_ckpt_mAP0.7649526596069336.pth'

n_trail = 10
n_epoch = 1
