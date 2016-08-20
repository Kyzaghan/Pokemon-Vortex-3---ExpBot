# -*- coding: utf-8 -*-
import json


def settings_reader(x):
    """Json parser for settings file
    :param x: Config file
    :return:
    """
    with open('Config/' + x, encoding='utf-8') as data_file:
        read_data = data_file.read()
        data_file.closed
    data = json.loads(read_data)
    return data


def settings_reader_general(x):
    """Json parser for settings file
    :param x: Json file
    :return:
    """
    with open(x, encoding='utf-8') as data_file:
        read_data = data_file.read()
        data_file.closed
    data = json.loads(read_data)
    return data


def read_authentication():
    """Read Auth Information
    :return: data
    """
    return settings_reader('authentication.json')


def read_config():
    """Read Config Information
    :return: data
    """
    return settings_reader('config.json')


def read_map():
    """Read Map Information
    :return: data
    """
    return settings_reader('map.json')


def read_legys():
    """Read Legendary Pokémon Information
    :return: data
    """
    return settings_reader('legy.json')


def read_pokys():
    """Read Normal Pokémon Information
    :return: data
    """
    return settings_reader('poky.json')


def read_trans(lang):
    """Read Translations
    :return: data
    """
    return settings_reader('Translation/translation.' + lang)


def config_copy(config, old_config):
    """
    :param config: New config file
    :param old_config: Old config file
    """
    data = settings_reader_general(config)
    old_data = settings_reader_general(old_config)
    for key, value in data.items():
        if old_data[key] is not None and key != "Version":
            data[key] = old_data[key]
    json.dump(data, open(config, "w"))
