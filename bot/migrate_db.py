from data.storage import DatabaseManager
db = DatabaseManager()

# db.query('ALTER TABLE users ADD COLUMN account_state INTEGER DEFAULT 0')
# db.query("ALTER TABLE users ADD COLUMN referral_id TEXT DEFAULT ''")

different_model_names = {
    'Toyota': {
        '4_runner': '4runner',
        'chr': 'c-hr',
        'prius_c': 'prius',
        'prius_v': 'prius',
        'rav_4': 'rav4',
    },
    'Lexus': {
        'gx_460': 'gx460'
    },
    'VAZ (Lada)': {
        '2121_(niva)': '2121_niva',
        "2121_(4x4)": "2121_niva",
        "2131_(4x4)": "2131_niva"
    },
    'Hyundai': {
        'elantra_gt': 'elantra',
        'ix_35': 'ix35',
        'lantra': 'elantra',
        'h_1': 'h-1',
        "i_10":'i10',
        "i_20":'i20',
        "i_30":'i30',
        "i_35":'i35',
        "i_40":'i40'
    },
    'Mitsubishi': {
        'l_200': 'l200'
    },
    'Land Rover': {
        'land_rover_sport': 'range_rover_sport',
        'range_rover__velar': 'range_rover_velar'
    },
    'Ford': {
        'f150': 'f-150',
        "f250": 'f-250',
        "f350": 'f-350',
        "f450": 'f-450',
        'taunus': 'taurus',
        "focus": "focus_(north_america)",
        "fusion": "fusion_(north_america)"
    },
    'Nissan': {
        'x-terra': 'xterra',
        "370_z": "370z",
        "nv_200": "nv200"
    },
    'Honda': {
        'step_wagon': 'stepwgn',
        "odyssey": "odyssey_(north_america)"
    },
    'Suzuki': {
        'sx_4': 'sx4'
    },
    'Infiniti': {
        'qx_30': 'qx30',
        'ex_35': 'ex35',
        'fx_35': 'fx35',
        'fx_37': 'fx37',
        'g_35': 'g35',
        'g_37': 'g37',
        'm_35': 'm35',
        'q_50': 'q50',
        'q_60': 'q60',
        'qx_4': 'qx4',
        'qx_50': 'qx50',
        'qx_56': 'qx56',
        'qx_60': 'qx60',
        'qx_70': 'qx70',
        'qx_80': 'qx80',
        "fx_45": 'fx45',
        "fx_50": 'fx50',
        "g_20":"g20",
        "g_25":"g25",
        "jx_35":"jx35",
        "m_37":"m37"
    },
    'Volvo': {
        's_40': 's40',
        's_60': 's60',
        's_80': 's80',
        "s_70": "s70",
        "s_90": "s90",
        "v_40": "v40",
        "v_60": "v60",
        "xc_40":"xc40",
        'xc_60':'xc60',
        'xc_90':'xc90'
    },
    'Chrysler': {
        '300': '300c',
        'town_and_country': 'town_&_country'
    },
    'Hummer': {
        'h_2': 'h2',
        'h_3': 'h3'
    },
    "GAZ (ГАЗ)":{
        "21": "21_volga",
        "24": "24_volga",
        "310221": "310221_volga",
        "31029": "31029_volga",
        "3110": "3110_volga",
        "3111": "3111_volga",
        "3102": "3102_volga",
        "3105": "3105_volga",
        "31105": "31105_volga"
    },
    "Jeep":{
        "liberty": "liberty_(north_america)",
        "patriot": "liberty_(patriot)"
    },
    'Mazda':{
        "mazda_2":'2',
        "mazda_3":'3',
        "mazda_5":'5',
        "mazda_6":'6',
        "familia_wagon": 'familia'
    },
    'Mitsubishi':{
        "l_300": "l300"
    },
    'Volkswagen':{
        "id_3":"id.3",
        "id_4":"id.4",
        "id_5":"id.5",
        "id_6":"id.6",
        "passat": "passat_(north_america)"
    },
    "Mercedes-Benz":{
        '190' : "190_(w201)",
        "a_140":"a-class",
        "a_150":"a-class",
        "a_160":"a-class",
        "a_170":"a-class",
        "a_180":"a-class",
        "a_190":"a-class",
        "a_200":"a-class",
        "a_210":"a-class",
        "a_220":"a-class",

        "b_150":"b-class",
        "b_170":"b-class",
        "b_180":"b-class",
        "b_200":"b-class",
        "b_220":"b-class",
        "b_250":"b-class",
    
        "c_180":"c-class",
        "c_200":"c-class",
        "c_220":"c-class",
        "c_230":"c-class",
        "c_240":"c-class",
        "c_250":"c-class",
        "c_270":"c-class",
        "c_280":"c-class",
        "c_300":"c-class",
        "c_30_amg":"c-class_amg",
        "c_320":"c-class",
        "c_32_amg":"c-class_amg",
        "c_350":"c-class",
        "c_400":"c-class",
        "c_43_amg":"c-class_amg",
        "c_450_amg":"c-class_amg",
        "c_55_amg":"c-class_amg",
        "c_63_amg":"c-class_amg",
    
        "citan_108":'citan',
        "citan_109":'citan',
        "citan_112":'citan',

        "cl_500":"cl-class",
        "cl_550":"cl-class",
        "cl_55_amg":"cl-class_amg",

        "cla_180":"cla-class",
        "cla_200":"cla-class",
        "cla_250":"cla-class",
        "cla_45_amg":"cla-class_amg",

        "clc_180": 'clc-class',

        "clk_200":"clk-class",
        "clk_220":"clk-class",
        "clk_230":"clk-class",
        "clk_240":"clk-class",
        "clk_270":"clk-class",
        "clk_320":"clk-class",
        "clk_350":"clk-class",
        "clk_500":"clk-class",
        "clk_550":"clk-class",
        "clk_63_amg":"clk-class_amg",
    
        "cls_320":"cls-class",
        "cls_350":"cls-class",
        "cls_450":"cls-class",
        "cls_500":"cls-class",
        "cls_550":"cls-class",
        "cls_55_amg":"cls-class_amg",
        "cls_63_amg":"cls-class_amg",

        "e_190":"e-class",
        "e_200":"e-class",
        "e_210":"e-class",
        "e_220":"e-class",
        "e_230":"e-class",
        "e_240":"e-class",
        "e_250":"e-class",
        "e_260":"e-class",
        "e_270":"e-class",
        "e_280":"e-class",
        "e_290":"e-class",
        "e_300":"e-class",
        "e_320":"e-class",
        "e_350":"e-class",
        "e_36_amg":"e-class_amg",
        "e_400":"e-class",
        "e_420":"e-class",
        "e_430":"e-class",
        "e_450":"e-class",
        "e_500":"e-class",
        "e_55":"e-class",
        "e_550":"e-class",
        "e_63_amg":"e-class_amg",
        "eqb_350":"e-class",
    
         "g_320":"g-class",
         "g_350":"g-class",
         "g_400":"g-class",
         "g_500":"g-class",
         "g_550":"g-class",
         "g_55_amg":"g-class_amg",
         "g_63_amg":"g-class_amg",

        "gl_320":"gl-class", 
        "gl_350":"gl-class", 
        "gl_420":"gl-class", 
        "gl_450":"gl-class", 
        "gl_550":"gl-class", 
        "gl_63_amg":"gl-class_amg", 

        "gla_180":"gla-class",
        "gla_200":"gla-class",
        "gla_250":"gla-class",
        "gla_350":"gla-class",
        "gla_45_amg":"gla-class_amg",
    
        "glb_250": "glb-class", 

        "glc":"glc-class",
        "glc_220":"glc-class",
        "glc_250":"glc-class",
        "glc_300":"glc-class",
        "glc_350":"glc-class",
        "glc_43_amg":"glc-class",
        "glc_63_amg":"glc-class",
        "glc_coupe":"glc-class",
        "glc_coupe_amg":"glc-class",
    
        "gle":"gle-class",
        "gle_250":"gle-class",
        "gle_350":"gle-class",
        "gle_400":"gle-class",
        "gle_43_amg":"gle-class",
        "gle_450":"gle-class",
        "gle_450_amg":"gle-class",
        "gle_53":"gle-class",
        "gle_550e":"gle-class",
        "gle_63_amg":"gle-class",
        "gle_coupe":"gle-class",
        "gle_coupe_amg":"gle-class",
    
        "glk_250":"glk-class",
        "glk_350":"glk-class",
        
        "gls_350":"gls-class",
        "gls_400_d":"gls-class",
        "gls_450":"gls-class",
        "gls_450_amg":"gls-class_amg",
        "gls_550":"gls-class",
        "gls_600":"gls-class",
        "gls_63_amg":"gls-class_amg",

        "ml_230":"ml",
        "ml_250":"ml",
        "ml_270":"ml",
        "ml_280":"ml",
        "ml_300":"ml",
        "ml_320":"ml",
        "ml_350":"ml",
        "ml_400":"ml",
        "ml_430":"ml",
        "ml_500":"ml",
        "ml_550":"ml",
        "ml_55_amg":"ml",
        "ml_63_amg":"ml",
    
        "r_320":"r-class",
        "r_350":"r-class",
    
        "s-klas_(w126)":"s-class",
        "s_280":"s-class",
        "s_300":"s-class",
        "s_320":"s-class",
        "s_350":"s-class",
        "s_400":"s-class",
        "s_420":"s-class",
        "s_430":"s-class",
        "s_450":"s-class",
        "s_500":"s-class",
        "s_55":"s-class",
        "s_550":"s-class",
        "s_560":"s-class",
        "s_580":"s-class",
        "s_600":"s-class",
        "s_63_amg":"s-class_amg",

        "sl_280":"sl-class",
        "sl_300":"sl-class",
        "sl_350":"sl-class",
        "sl_380":"sl-class",
        "sl_500":"sl-class",
    
        "slk_200":"slk-class",
        "slk_250":"slk-class",
        "slk_350":"slk-class",
    
        "v_200":"v-class",
        "v_220":"v-class",
        "v_230":"v-class",
        "v_250":"v-class",
        "v_300":"v-class"
    },
    'Lexus':{
        "ct_200_h": "ct", 

        "es_250":"es",
        "es_300":"es",
        "es_330":"es",
        "es_350":"es",
    
        "gs_300":"gs",
        "gs_350":"gs",
        "gs_450":"gs",
        "gs_460":"gs",
    
        "gx_470":"gx",
    
        "is_200":"is",
        "is_220":"is",
        "is_250":"is",
        "is_300":"is",
        "is_350":"is",
    
        "ls_430":"ls",
        "ls_460":"ls",
        "ls_500":"ls",
        "ls_500_h":"ls",
    
        "lx_450":"lx",
        "lx_470":"lx",
        "lx_500":"lx",
        "lx_570":"lx",
        "lx_600":"lx",
    
        "nx_200":"nx",
        "nx_250":"nx",
        "nx_300":"nx",
        "nx_350":"nx",
    
        "rx_300":"rx",
        "rx_330":"rx",
        "rx_350":"rx",
        "rx_400":"rx",
        "rx_450":"rx",
    
        "ux_200":"ux",
        "ux_250_h":"ux",
    },
    
    'BMW': {
        "114":"1_series",
        "116":"1_series",
        "118":"1_series",
        "120":"1_series",
        "123":"1_series",
        "128":"1_series",
        "135":"1_series",
        
        "220":"2_series",
        "225":"2_series",
        "228":"2_series",
        
        "316":"3_series",
        "318":"3_series",
        "320":"3_series",
        "320_gran_turismo":"3_series",
        "323":"3_series",
        "325":"3_series",
        "326":"3_series",
        "328":"3_series",
        "330":"3_series",
        "335":"3_series",
        "340":"3_series",
        
        "418":"4_series",
        "420":"4_series",
        "428":"4_series",
        "430":"4_series",
        "435":"4_series",
        "440":"4_series",
    
        "518":"5_series",
        "520":"5_series",
        "523":"5_series",
        "525":"5_series",
        "528":"5_series",
        "530":"5_series",
        "530d_gran_turismo":"5_series",
        "535":"5_series",
        "535i_gran_turismo":"5_series",
        "540":"5_series",
        "545":"5_series",
        "550":"5_series",
        "550i_gran_turismo":"5_series",
    
        "635":"6_series",
        "640":"6_series",
        "645":"6_series",
        "650":"6_series",
    
        "728":"7_series",
        "730":"7_series",
        "735":"7_series",
        "740":"7_series",
        "745":"7_series",
        "750":"7_series",
    
        "840":"8_series",
        "850":"8_series"
    }
}

import pandas as pd

import sqlite3

conn = sqlite3.connect('data.db')

for brand, models in different_model_names.items():
    for old_name, new_name in models.items():
        conn.execute(f"UPDATE listings SET model = ? WHERE website = 'myauto.ge' AND car_brand = ? AND model = ?;",
                     (new_name, brand, old_name))



conn.execute(f"UPDATE listings SET interior_color = 'blue' WHERE interior_color = 'cyan';")

conn.execute(f"UPDATE listings SET gas_equipment = 'no' WHERE gas_equipment = 0;")
conn.execute(f"UPDATE listings SET gas_equipment = 'installed' WHERE gas_equipment = 1;")

conn.commit()

conn.close()

db.query("UPDATE saved_cars SET found_cars = '[]' WHERE found_cars ='{}';")
db.conn.close()