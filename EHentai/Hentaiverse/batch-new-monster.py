#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:  GNU AFFERO GENERAL PUBLIC LICENSE Version 3
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvMonsterAvatar
# @file: batch-new-monster.py
# @time: 2021/5/23 13:34
# @desc: New a Monster and RENAME

import requests
import re
import json
import time
from bs4 import BeautifulSoup as Bs

config = json.load(open('config.json'))
HvLoginURL = f"http://alt.hentaiverse.org/login?ipb_member_id={config['ipb_member_id']}&ipb_pass_hash={config['ipb_pass_hash']}"


def create_new(m_class='giant', m_patk='crsh'):
    if m_patk == 'crushing':
        if m_class not in [
            'arthropod',
            'dragonkin',
            'giant',
            'humanoid',
                'undead']:
            return False
    elif m_patk == 'piercing':
        if m_class not in [
            'arthropod',
            'avion',
            'beast',
            'daimon',
            'dragonkin',
            'humanoid',
            'mechanoid',
            'reptilian',
                'sprite']:
            return False
    elif m_patk in ['fire', 'elec', 'wind', 'cold']:
        if m_class != 'elemental':
            return False

    def m_patk(x): return {
        x == 'crushing': 'crsh',
        x == 'piercing': 'prcg',
        x == 'slashing': 'slsh',
        x in ['fire', 'elec', 'wind', 'cold']: x
    }

    def m_class(x): return {
        x == 'arthropod': 1,
        x == 'avion': 2,
        x == 'beast': 3,
        x == 'celestial': 4,
        x == 'daimon': 5,
        x == 'dragonkin': 6,
        x == 'elemental': 7,
        x == 'giant': 8,
        x == 'humanoid': 10,
        x == 'mechanoid': 12,
        x == 'reptilian': 13,
        x == 'sprite': 14,
        x == 'undead': 15
    }
    resp = session.post(
        'http://alt.hentaiverse.org/?s=Bazaar&ss=ml&create=new',
        data={
            'selected_class': m_class,
            'selected_patk': m_patk})
    resp = Bs(resp.text, 'html.parser')
    if resp.find('div', id='monsterstats_rename'):
        return True
    else:
        return False


def feed_and_drug(slot_id):
    url = f'http://alt.hentaiverse.org/?s=Bazaar&ss=ml&slot={slot_id}'
    session.post(url, data={'food_action': 'food'})
    session.post(url, data={'food_action': 'drugs'})
    resp = session.get(url)
    resp = Bs(resp.text, 'html.parser')
    if not resp.find('img', src='/y/monster/feedmonster_d.png'):
        return 3
    elif not resp.find('img', src='/y/monster/drugmonster_d.png'):
        return 2
    else:
        return True


def upgrade(slot_id, pa=None, em=None):
    if pa:
        session.post(
            f'http://alt.hentaiverse.org/?s=Bazaar&ss=ml&slot={slot_id}',
            data={
                'crystal_upgrade': f'pa_{pa}'})
    else:
        session.post(
            f'http://alt.hentaiverse.org/?s=Bazaar&ss=ml&slot={slot_id}',
            data={
                'crystal_upgrade': f'er_{em}'})


def upgrade_to_lv25(slot_id, ex_types='str'):
    primary_attributes = ['str', 'dex', 'agi', 'end', 'int', 'wis']
    elemental_mitigation = ['fire', 'cold', 'elec', 'wind', 'holy', 'dark']
    for pa in primary_attributes:
        upgrade(slot_id, pa=pa)
    for em in elemental_mitigation:
        upgrade(slot_id, em=em)
    if ex_types in primary_attributes:
        upgrade(slot_id, pa=ex_types)
    elif ex_types in elemental_mitigation:
        upgrade(slot_id, em=ex_types)
    else:
        return False
    return True


def rename(slot_id, name):
    url = f'http://alt.hentaiverse.org/?s=Bazaar&ss=ml&slot={slot_id}'
    resp = session.get(url)
    resp = Bs(resp.text, 'html.parser')
    assert resp.find('img', src='/y/monster/rename.png')
    session.post(url, data={
        'rename_monster': name})
    return True


def delete(slot_id):
    url = f'http://alt.hentaiverse.org/?s=Bazaar&ss=ml&slot={slot_id}'
    resp = session.get(url)
    resp = Bs(resp.text, 'html.parser')
    scripts = resp.find_all("script", type="text/javascript")
    for script in scripts:
        out = (
            re.findall(
                r'e\("delete_monster"\).value = \"(.*?)\";',
                str(script)))
        if out:
            session.post(url, data={
                'delete_monster': out[0]})
            return out[0], 0
    return False


if __name__ == '__main__':
    session = requests.Session()
    session.get(HvLoginURL)

    for i in range(126, 149):
        time_now = str(
            time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime()) +
            " 怪物编号" +
            str(i))
        # delete_token, status = delete(i)
        # if status == 0:
        #     time_now += f" 怪物删除{delete_token}"
        if create_new(m_class='gaint', m_patk='crsh'):
            time_now += " 怪物创建完成"
        if feed_and_drug(i):
            time_now += " 怪物喂食完成"
        if upgrade_to_lv25(i):
            time_now += " 怪物升级完成"
        name = f"JK BEST {i}"
        if rename(i, name):
            time_now += f" 怪物命名为{name}"
        print(time_now)
