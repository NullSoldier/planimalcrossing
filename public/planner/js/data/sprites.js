/** 
 * This file was auto-generated with object-generator.py 
 */

'use strict';

var data = {
    tiles: [
        'placeholder',
        'building-restriction',
        'object-restriction',
    ],
    buildings: {
        'police-station': {
            'sprite': 'img/tiles/buildings/police-station.png',
            'width': 48,
            'height': 48,
        },
        'train-station': {
            'sprite': 'img/tiles/buildings/train-station.png',
            'width': 80,
            'height': 32,
        },
        're-tail': {
            'sprite': 'img/tiles/buildings/re-tail.png',
            'width': 64,
            'height': 48,
        },
        'sign-board': {
            'sprite': 'img/tiles/buildings/sign-board.png',
            'width': 32,
            'height': 32,
        },
    },
    objects: [
        'road',
    ],
    map: [
        'rocks',
        'grass',
        'water',
        'sand',
    ]
};

// nodeJS would also like to use this file
if (typeof module !== 'undefined') {
    module.exports = data;
}

