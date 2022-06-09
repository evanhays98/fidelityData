import json
import time

import requests
import random
import os
import re

BASE_URL = 'http://localhost:8000/api'
logo = ['ad', 'address-book', 'address-card', 'adjust', 'air-freshener', 'align-center', 'align-justify', 'align-left',
        'align-right', 'allergies', 'ambulance', 'american-sign-language-interpreting', 'anchor', 'angle-double-down',
        'angle-double-left', 'angle-double-right', 'angle-double-up', 'angle-down', 'angle-left', 'angle-right',
        'angle-up', 'angry', 'ankh', 'apple-alt', 'archive', 'archway', 'arrow-alt-circle-down',
        'arrow-alt-circle-left', 'arrow-alt-circle-right', 'arrow-alt-circle-up', 'arrow-circle-down',
        'arrow-circle-left', 'arrow-circle-right', 'arrow-circle-up', 'arrow-down', 'arrow-left', 'arrow-right',
        'arrow-up', 'arrows-alt-h', 'arrows-alt-v', 'arrows-alt', 'assistive-listening-systems', 'asterisk', 'at',
        'atlas', 'atom', 'audio-description', 'award', 'baby-carriage', 'baby', 'backspace', 'backward', 'bacon',
        'bahai', 'balance-scale-left', 'balance-scale-right', 'balance-scale', 'ban', 'band-aid', 'barcode', 'bars',
        'baseball-ball', 'basketball-ball', 'bath', 'battery-empty', 'battery-full', 'battery-half', 'battery-quarter',
        'battery-three-quarters', 'bed', 'beer', 'bell-slash', 'bell', 'bezier-curve', 'bible', 'bicycle', 'biking',
        'binoculars', 'biohazard', 'birthday-cake', 'blender-phone', 'blender', 'blind', 'blog', 'bold', 'bolt', 'bomb',
        'bone', 'bong', 'book-dead', 'book-medical', 'book-open', 'book-reader', 'book', 'bookmark', 'border-all',
        'border-none', 'border-style', 'bowling-ball', 'box-open', 'box-tissue', 'box', 'boxes', 'braille', 'brain',
        'bread-slice', 'briefcase-medical', 'briefcase', 'broadcast-tower', 'broom', 'brush', 'bug', 'building',
        'bullhorn', 'bullseye', 'burn', 'bus-alt', 'bus', 'business-time', 'calculator', 'calendar-alt',
        'calendar-check', 'calendar-day', 'calendar-minus', 'calendar-plus', 'calendar-times', 'calendar-week',
        'calendar', 'camera-retro', 'camera', 'campground', 'candy-cane', 'cannabis', 'capsules', 'car-alt',
        'car-battery', 'car-crash', 'car-side', 'car', 'caravan', 'caret-down', 'caret-left', 'caret-right',
        'caret-square-down', 'caret-square-left', 'caret-square-right', 'caret-square-up', 'caret-up', 'carrot',
        'cart-arrow-down', 'cart-plus', 'cash-register', 'cat', 'certificate', 'chair', 'chalkboard-teacher',
        'chalkboard', 'charging-station', 'chart-area', 'chart-bar', 'chart-line', 'chart-pie', 'check-circle',
        'check-double', 'check-square', 'check', 'cheese', 'chess-bishop', 'chess-board', 'chess-king', 'chess-knight',
        'chess-pawn', 'chess-queen', 'chess-rook', 'chess', 'chevron-circle-down', 'chevron-circle-left',
        'chevron-circle-right', 'chevron-circle-up', 'chevron-down', 'chevron-left', 'chevron-right', 'chevron-up',
        'child', 'church', 'circle-notch', 'circle', 'city', 'clinic-medical', 'clipboard-check', 'clipboard-list',
        'clipboard', 'clock', 'clone', 'closed-captioning', 'cloud-download-alt', 'cloud-meatball', 'cloud-moon-rain',
        'cloud-moon', 'cloud-rain', 'cloud-showers-heavy', 'cloud-sun-rain', 'cloud-sun', 'cloud-upload-alt', 'cloud',
        'cocktail', 'code-branch', 'code', 'coffee', 'cog', 'cogs', 'coins', 'columns', 'comment-alt', 'comment-dollar',
        'comment-dots', 'comment-medical', 'comment-slash', 'comment', 'comments-dollar', 'comments', 'compact-disc',
        'compass', 'compress-alt', 'compress-arrows-alt', 'compress', 'concierge-bell', 'cookie-bite', 'cookie', 'copy',
        'copyright', 'couch', 'credit-card', 'crop-alt', 'crop', 'cross', 'crosshairs', 'crow', 'crown', 'crutch',
        'cube', 'cubes', 'cut', 'database', 'deaf', 'democrat', 'desktop', 'dharmachakra', 'diagnoses', 'dice-d20',
        'dice-d6', 'dice-five', 'dice-four', 'dice-one', 'dice-six', 'dice-three', 'dice-two', 'dice',
        'digital-tachograph', 'directions', 'disease', 'divide', 'dizzy', 'dna', 'dog', 'dollar-sign', 'dolly-flatbed',
        'dolly', 'donate', 'door-closed', 'door-open', 'dot-circle', 'dove', 'download', 'drafting-compass', 'dragon',
        'draw-polygon', 'drum-steelpan', 'drum', 'drumstick-bite', 'dumbbell', 'dumpster-fire', 'dumpster', 'dungeon',
        'edit', 'egg', 'eject', 'ellipsis-h', 'ellipsis-v', 'envelope-open-text', 'envelope-open', 'envelope-square',
        'envelope', 'equals', 'eraser', 'ethernet', 'euro-sign', 'exchange-alt', 'exclamation-circle',
        'exclamation-triangle', 'exclamation', 'expand-alt', 'expand-arrows-alt', 'expand', 'external-link-alt',
        'external-link-square-alt', 'eye-dropper', 'eye-slash', 'eye', 'fan', 'fast-backward', 'fast-forward', 'faucet',
        'fax', 'feather-alt', 'feather', 'female', 'fighter-jet', 'file-alt', 'file-archive', 'file-audio', 'file-code',
        'file-contract', 'file-csv', 'file-download', 'file-excel', 'file-export', 'file-image', 'file-import',
        'file-invoice-dollar', 'file-invoice', 'file-medical-alt', 'file-medical', 'file-pdf', 'file-powerpoint',
        'file-prescription', 'file-signature', 'file-upload', 'file-video', 'file-word', 'file', 'fill-drip', 'fill',
        'film', 'filter', 'fingerprint', 'fire-alt', 'fire-extinguisher', 'fire', 'first-aid', 'fish', 'fist-raised',
        'flag-checkered', 'flag-usa', 'flag', 'flask', 'flushed', 'folder-minus', 'folder-open', 'folder-plus',
        'folder', 'font-awesome-logo-full', 'font', 'football-ball', 'forward', 'frog', 'frown-open', 'frown',
        'funnel-dollar', 'futbol', 'gamepad', 'gas-pump', 'gavel', 'gem', 'genderless', 'ghost', 'gift', 'gifts',
        'glass-cheers', 'glass-martini-alt', 'glass-martini', 'glass-whiskey', 'glasses', 'globe-africa',
        'globe-americas', 'globe-asia', 'globe-europe', 'globe', 'golf-ball', 'gopuram', 'graduation-cap',
        'greater-than-equal', 'greater-than', 'grimace', 'grin-alt', 'grin-beam-sweat', 'grin-beam', 'grin-hearts',
        'grin-squint-tears', 'grin-squint', 'grin-stars', 'grin-tears', 'grin-tongue-squint', 'grin-tongue-wink',
        'grin-tongue', 'grin-wink', 'grin', 'grip-horizontal', 'grip-lines-vertical', 'grip-lines', 'grip-vertical',
        'guitar', 'h-square', 'hamburger', 'hammer', 'hamsa', 'hand-holding-heart', 'hand-holding-medical',
        'hand-holding-usd', 'hand-holding-water', 'hand-holding', 'hand-lizard', 'hand-middle-finger', 'hand-paper',
        'hand-peace', 'hand-point-down', 'hand-point-left', 'hand-point-right', 'hand-point-up', 'hand-pointer',
        'hand-rock', 'hand-scissors', 'hand-sparkles', 'hand-spock', 'hands-helping', 'hands-wash', 'hands',
        'handshake-alt-slash', 'handshake-slash', 'handshake', 'hanukiah', 'hard-hat', 'hashtag', 'hat-cowboy-side',
        'hat-cowboy', 'hat-wizard', 'hdd', 'head-side-cough-slash', 'head-side-cough', 'head-side-mask',
        'head-side-virus', 'heading', 'headphones-alt', 'headphones', 'headset', 'heart-broken', 'heart', 'heartbeat',
        'helicopter', 'highlighter', 'hiking', 'hippo', 'history', 'hockey-puck', 'holly-berry', 'home', 'horse-head',
        'horse', 'hospital-alt', 'hospital-symbol', 'hospital-user', 'hospital', 'hot-tub', 'hotdog', 'hotel',
        'hourglass-end', 'hourglass-half', 'hourglass-start', 'hourglass', 'house-damage', 'house-user', 'hryvnia',
        'i-cursor', 'ice-cream', 'icicles', 'icons', 'id-badge', 'id-card-alt', 'id-card', 'igloo', 'image', 'images',
        'inbox', 'indent', 'industry', 'infinity', 'info-circle', 'info', 'italic', 'jedi', 'joint', 'journal-whills',
        'kaaba', 'key', 'keyboard', 'khanda', 'kiss-beam', 'kiss-wink-heart', 'kiss', 'kiwi-bird', 'landmark',
        'language', 'laptop-code', 'laptop-house', 'laptop-medical', 'laptop', 'laugh-beam', 'laugh-squint',
        'laugh-wink', 'laugh', 'layer-group', 'leaf', 'lemon', 'less-than-equal', 'less-than', 'level-down-alt',
        'level-up-alt', 'life-ring', 'lightbulb', 'link', 'lira-sign', 'list-alt', 'list-ol', 'list-ul', 'list',
        'location-arrow', 'lock-open', 'lock', 'long-arrow-alt-down', 'long-arrow-alt-left', 'long-arrow-alt-right',
        'long-arrow-alt-up', 'low-vision', 'luggage-cart', 'lungs-virus', 'lungs', 'magic', 'magnet', 'mail-bulk',
        'male', 'map-marked-alt', 'map-marked', 'map-marker-alt', 'map-marker', 'map-pin', 'map-signs', 'map', 'marker',
        'mars-double', 'mars-stroke-h', 'mars-stroke-v', 'mars-stroke', 'mars', 'mask', 'medal', 'medkit', 'meh-blank',
        'meh-rolling-eyes', 'meh', 'memory', 'menorah', 'mercury', 'meteor', 'microchip', 'microphone-alt-slash',
        'microphone-alt', 'microphone-slash', 'microphone', 'microscope', 'minus-circle', 'minus-square', 'minus',
        'mitten', 'mobile-alt', 'mobile', 'money-bill-alt', 'money-bill-wave-alt', 'money-bill-wave', 'money-bill',
        'money-check-alt', 'money-check', 'monument', 'moon', 'mortar-pestle', 'mosque', 'motorcycle', 'mountain',
        'mouse-pointer', 'mouse', 'mug-hot', 'music', 'network-wired', 'neuter', 'newspaper', 'not-equal',
        'notes-medical', 'object-group', 'object-ungroup', 'oil-can', 'om', 'otter', 'outdent', 'pager', 'paint-brush',
        'paint-roller', 'palette', 'pallet', 'paper-plane', 'paperclip', 'parachute-box', 'paragraph', 'parking',
        'passport', 'pastafarianism', 'paste', 'pause-circle', 'pause', 'paw', 'peace', 'pen-alt', 'pen-fancy',
        'pen-nib', 'pen-square', 'pen', 'pencil-alt', 'pencil-ruler', 'people-arrows', 'people-carry', 'pepper-hot',
        'percent', 'percentage', 'person-booth', 'phone-alt', 'phone-slash', 'phone-square-alt', 'phone-square',
        'phone-volume', 'phone', 'photo-video', 'piggy-bank', 'pills', 'pizza-slice', 'place-of-worship',
        'plane-arrival', 'plane-departure', 'plane-slash', 'plane', 'play-circle', 'play', 'plug', 'plus-circle',
        'plus-square', 'plus', 'podcast', 'poll-h', 'poll', 'poo-storm', 'poo', 'poop', 'portrait', 'pound-sign',
        'power-off', 'pray', 'praying-hands', 'prescription-bottle-alt', 'prescription-bottle', 'prescription', 'print',
        'procedures', 'project-diagram', 'pump-medical', 'pump-soap', 'puzzle-piece', 'qrcode', 'question-circle',
        'question', 'quidditch', 'quote-left', 'quote-right', 'quran', 'radiation-alt', 'radiation', 'rainbow',
        'random', 'receipt', 'record-vinyl', 'recycle', 'redo-alt', 'redo', 'registered', 'remove-format', 'reply-all',
        'reply', 'republican', 'restroom', 'retweet', 'ribbon', 'ring', 'road', 'robot', 'rocket', 'route',
        'rss-square', 'rss', 'ruble-sign', 'ruler-combined', 'ruler-horizontal', 'ruler-vertical', 'ruler', 'running',
        'rupee-sign', 'sad-cry', 'sad-tear', 'satellite-dish', 'satellite', 'save', 'school', 'screwdriver', 'scroll',
        'sd-card', 'search-dollar', 'search-location', 'search-minus', 'search-plus', 'search', 'seedling', 'server',
        'shapes', 'share-alt-square', 'share-alt', 'share-square', 'share', 'shekel-sign', 'shield-alt', 'shield-virus',
        'ship', 'shipping-fast', 'shoe-prints', 'shopping-bag', 'shopping-basket', 'shopping-cart', 'shower',
        'shuttle-van', 'sign-in-alt', 'sign-language', 'sign-out-alt', 'sign', 'signal', 'signature', 'sim-card',
        'sitemap', 'skating', 'skiing-nordic', 'skiing', 'skull-crossbones', 'skull', 'slash', 'sleigh', 'sliders-h',
        'smile-beam', 'smile-wink', 'smile', 'smog', 'smoking-ban', 'smoking', 'sms', 'snowboarding', 'snowflake',
        'snowman', 'snowplow', 'soap', 'socks', 'solar-panel', 'sort-alpha-down-alt', 'sort-alpha-down',
        'sort-alpha-up-alt', 'sort-alpha-up', 'sort-amount-down-alt', 'sort-amount-down', 'sort-amount-up-alt',
        'sort-amount-up', 'sort-down', 'sort-numeric-down-alt', 'sort-numeric-down', 'sort-numeric-up-alt',
        'sort-numeric-up', 'sort-up', 'sort', 'spa', 'space-shuttle', 'spell-check', 'spider', 'spinner', 'splotch',
        'spray-can', 'square-full', 'square-root-alt', 'square', 'stamp', 'star-and-crescent', 'star-half-alt',
        'star-half', 'star-of-david', 'star-of-life', 'star', 'step-backward', 'step-forward', 'stethoscope',
        'sticky-note', 'stop-circle', 'stop', 'stopwatch-20', 'stopwatch', 'store-alt-slash', 'store-alt',
        'store-slash', 'store', 'stream', 'street-view', 'strikethrough', 'stroopwafel', 'subscript', 'subway',
        'suitcase-rolling', 'suitcase', 'sun', 'superscript', 'surprise', 'swatchbook', 'swimmer', 'swimming-pool',
        'synagogue', 'sync-alt', 'sync', 'syringe', 'table-tennis', 'table', 'tablet-alt', 'tablet', 'tablets',
        'tachometer-alt', 'tag', 'tags', 'tape', 'tasks', 'taxi', 'teeth-open', 'teeth', 'temperature-high',
        'temperature-low', 'tenge', 'terminal', 'text-height', 'text-width', 'th-large', 'th-list', 'th',
        'theater-masks', 'thermometer-empty', 'thermometer-full', 'thermometer-half', 'thermometer-quarter',
        'thermometer-three-quarters', 'thermometer', 'thumbs-down', 'thumbs-up', 'thumbtack', 'ticket-alt',
        'times-circle', 'times', 'tint-slash', 'tint', 'tired', 'toggle-off', 'toggle-on', 'toilet-paper-slash',
        'toilet-paper', 'toilet', 'toolbox', 'tools', 'tooth', 'torah', 'torii-gate', 'tractor', 'trademark',
        'traffic-light', 'trailer', 'train', 'tram', 'transgender-alt', 'transgender', 'trash-alt', 'trash-restore-alt',
        'trash-restore', 'trash', 'tree', 'trophy', 'truck-loading', 'truck-monster', 'truck-moving', 'truck-pickup',
        'truck', 'tshirt', 'tty', 'tv', 'umbrella-beach', 'umbrella', 'underline', 'undo-alt', 'undo',
        'universal-access', 'university', 'unlink', 'unlock-alt', 'unlock', 'upload', 'user-alt-slash', 'user-alt',
        'user-astronaut', 'user-check', 'user-circle', 'user-clock', 'user-cog', 'user-edit', 'user-friends',
        'user-graduate', 'user-injured', 'user-lock', 'user-md', 'user-minus', 'user-ninja', 'user-nurse', 'user-plus',
        'user-secret', 'user-shield', 'user-slash', 'user-tag', 'user-tie', 'user-times', 'user', 'users-cog', 'users',
        'utensil-spoon', 'utensils', 'vector-square', 'venus-double', 'venus-mars', 'venus', 'vial', 'vials',
        'video-slash', 'video', 'vihara', 'virus-slash', 'virus', 'viruses', 'voicemail', 'volleyball-ball',
        'volume-down', 'volume-mute', 'volume-off', 'volume-up', 'vote-yea', 'vr-cardboard', 'walking', 'wallet',
        'warehouse', 'water', 'wave-square', 'weight-hanging', 'weight', 'wheelchair', 'wifi', 'wind', 'window-close',
        'window-maximize', 'window-minimize', 'window-restore', 'wine-bottle', 'wine-glass-alt', 'wine-glass',
        'won-sign', 'wrench', 'x-ray', 'yen-sign', 'yin-yang']
colLogo = ["rgb(250,145,145)", "rgb(180,242,225)", "rgb(255,233,197)"]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def addUser(data):
    try:
        r = requests.post(
            BASE_URL + '/auth/sign-up',
            data
        )
        return r.json()['access_token']
    except requests.exceptions.RequestException as error:
        print()
        print(bcolors.FAIL + "Error: ", error.response + " : addUser")
        exit(2)


def addCompany(content, file, token):
    try:
        r = requests.post(BASE_URL + '/companies',
                          files={'file': open(file, 'rb')},
                          data={'createCompanyDto': content},
                          headers={"Authorization": "Bearer " + token}
                          )
        return r.json()['id']
    except requests.exceptions.RequestException as error:
        print()
        print(bcolors.FAIL + "Error: ", error.response + " : addCompany")
        exit(2)


def addOffer(content, file, token):
    try:
        requests.post(BASE_URL + '/offers',
                      files={'picture': open(file, 'rb')},
                      data={'dto': content},
                      headers={"Authorization": "Bearer " + token}
                      )
    except requests.exceptions.RequestException as error:
        print()
        print(bcolors.FAIL + "Error: ", error.response + " : addOffer")
        exit(2)


def main(userNum, companyNum, debug=0):
    fileUserName = open('Data/userName', 'r')
    fileEmail = open('Data/email', 'r')
    fileAddress = open('Data/address', 'r')
    fileCity = open('Data/city', 'r')
    fileCompanyName = open('Data/companyName', 'r')
    filePhone = open('Data/phone', 'r')
    fileZipCode = open('Data/zipCode', 'r')
    fileCountry = open('Data/country', 'r')

    userNameList = []
    for value in fileUserName.read().splitlines():
        userNameList.append(value)
    fileUserName.close()
    emailList = []
    for value in fileEmail.read().splitlines():
        emailList.append(value)
    fileEmail.close()
    addressList = []
    for value in fileAddress.read().splitlines():
        addressList.append(value)
    fileAddress.close()
    cityList = []
    for value in fileCity.read().splitlines():
        cityList.append(value)
    fileCity.close()
    companyNameList = []
    for value in fileCompanyName.read().splitlines():
        companyNameList.append(value)
    fileCompanyName.close()
    phoneList = []
    for value in filePhone.read().splitlines():
        phoneList.append(value)
    filePhone.close()
    zipCodeList = []
    for value in fileZipCode.read().splitlines():
        zipCodeList.append(value)
    fileZipCode.close()
    countryList = []
    for value in fileCountry.read().splitlines():
        countryList.append(value)
    fileCountry.close()
    imageList = os.listdir('Data/BusinessImage')
    imageList.sort(key=natural_keys)

    companyAdded = 0
    for i in range(debug, userNum + debug):
        data = {
            'userName': userNameList[i],
            'email': emailList[i],
            'password': 'Password1!'
        }
        access_token = addUser(data)
        print(bcolors.OKCYAN + "user " + userNameList[i] + " added successfully")

        r1 = random.randint(0, 10)
        if r1 > 9:
            r1 = 3
        elif r1 >= 7:
            r1 = 2
        else:
            r1 = 1

        if companyNum - 1 >= companyAdded:
            for j in range(r1):
                if companyNum - 1 <= companyAdded:
                    break
                data = '{"name": "'
                data += companyNameList[companyAdded]
                data += '", "address": { "city": "'
                data += cityList[companyAdded]
                data += '", "country": "'
                data += countryList[companyAdded]
                data += '", "fullAddress": "'
                data += addressList[companyAdded]
                data += '", "postalCode": "'
                data += '78760'
                data += '"}, "phoneNumber": "'
                data += '+33648487290'
                data += '", "logoName": "'
                r = random.randint(0, len(logo) - 1)
                data += logo[r]
                data += '", "logoColor": "'
                r = random.randint(0, 2)
                data += colLogo[r]
                data += '"}'
                companyId = addCompany(data, 'Data/BusinessImage/' + imageList[companyAdded], access_token)
                companyAdded += 1
                print(bcolors.OKCYAN + "     company " + companyNameList[companyAdded - 1] + " added successfully")

                r2 = random.randint(3, 7)
                for k in range(r2):
                    data = '{ "name": "'
                    r = random.randint(10, 25)
                    point = random.randint(7, 50)
                    data += str(point) + "%"
                    data += '","expirationDate": "2022-11-' + str(r)
                    data += '", "pointRequired" : ' + str(point)
                    data += ', "description": "'
                    data += 'Béneficier de ' + str(point) + '% chez '
                    data += companyNameList[companyAdded - 1]
                    data += " dans une large selection de produit que vous pouvez "
                    data += "retrouver sur notre site à l'address suivante https://www.google.com"
                    data += '", "companyId": "'
                    data += companyId + '"}'
                    addOffer(data, 'Data/OfferImage/offrePourcent.png', access_token)
                    print(bcolors.OKCYAN + "             offer " + str(point) + "%" + " added successfully")
    print(bcolors.OKGREEN + "everything has been added successfuly")


def addAllCompany():
    pass


main(3, 50, 0)

'''access_token = addUser({
    'userName': 'Evan',
    'email': 'sdda.fe@gmail.com',
    'password': 'Password1!'
})

data = """
        {"name": "La boite de nuit",
         "address": {
             "city": "Paris",
             "country": "France",
             "fullAddress": "111 rue JB Charcot",
             "postalCode": "13720"
         },
         "phoneNumber": "+330669660132",
         "logoName": "ad",
         "logoColor": "rgb(5,5,4)"
         }"""


companyId = addCompany(
    data,
    'Data/BusinessImage/business1.jpg',
    access_token
)

data = """
{
    "name": "pizaa 30%",
    "expirationDate": "2015-01-01",
    "pointRequired": 12,
    "description": "Béneficier de 30%",
    "companyId": """
data += '"'
data += companyId
data += '"}'

addOffer(data, 'Data/OfferImage/offrePourcent.png', access_token)'''
'''companyId = "b2ee0a02-269d-4a7b-8a49-3abce79a2a25"
data = '{ "name": "'
r = random.randint(10, 25)
point = random.randint(7, 50)
data += str(point) + "%"
data += '","expirationDate": "2022-11-' + str(r)
data += '", "pointRequired" : ' + str(point)
data += ', "description": "'
data += 'Béneficier de ' + str(point) + '% chez '
data += 'Amazon'
data += " dans une large selection de produit que vous pouvez "
data += "retrouver sur notre site à l'address suivante https://www.google.com"
data += '", "companyId": "'
data += companyId + '"}'

print(json.loads(data))'''
