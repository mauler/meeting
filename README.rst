=======
Meeting
=======

.. image:: https://img.shields.io/pypi/v/meeting.svg
        :target: https://pypi.python.org/pypi/meeting

.. image:: https://travis-ci.org/mauler/meeting.svg?branch=master
        :target: https://travis-ci.org/mauler/meeting

.. image:: https://ci.appveyor.com/api/projects/status/github/mauler/meeting?branch=master
        :target: https://ci.appveyor.com/project/mauler/meeting/branch/master

.. image:: https://codecov.io/github/mauler/meeting/coverage.svg?branch=master
        :target: https://codecov.io/github/mauler/meeting?branch=master

.. image:: https://badges.gitter.im/Join Chat.svg
        :target: https://gitter.im/mauler/meeting?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://readthedocs.org/projects/meeting/badge/?version=latest
        :target: https://readthedocs.org/projects/meeting/?badge=latest
        :alt: Documentation Status

.. image:: https://landscape.io/github/mauler/meeting/master/landscape.svg?style=flat
        :target: https://landscape.io/github/mauler/meeting/master
        :alt: Code Health

.. image:: https://img.shields.io/scrutinizer/g/mauler/meeting.svg
        :target: https://scrutinizer-ci.com/g/mauler/meeting/?branch=master
        :alt: Scrutinizer Code Quality


*****
O que é meeting ?
*****

É um sistema cashless, para isso foi criada toda uma suit.


Festival management application: Tickets E-Commerce, Tickets validation on Lobby (Web, Paper, Guest, Local Purchase) and Sells on Wristband/Card (Beverage, Food, Souvenir, etc).

É uma suit de aplicações para ter controle de um festival desde de a parte de vendas de tickets, controle de portaria e credenciamento e gerenciamento de vendas de produtos.

As aplicações foram criadas para funcionar em conjunto, porém é possível usa-las separadamente e até mesmo com aplicações de terceiros. É possível carregar o o lote de ingresoss físicos, assim como virtuais de outro sistema de vendas.


*****
Caso de uso que foi moldado
*****

O sistema foi usado 2x em um festival com cerca de 500 pagantes e 200 pessoas de crew e convidados.

O setup foi usar o gate em 1 notebook na portaria (Sem acesso nenhum na internet) comunicando com a rede interna do sistema festival para sincronizar as entradas.

O sistema de vendas foi usado no bar principal e parceiros de meerchandising, o sistema é cashless.


****
Forma correta de uso
****

Usar em rede local, pelo menos a aplicação festival não é interessante que tudo passe pela internet a não ser que você possua uma estrutura de internet muito boa.



The Gate Application
you can use
comandos que podem ser executados

conceitos e modelos

funciona com aplicação shop nao soh do meeting se obedecer os padroes


The Festival Application

conceito dos modelos, ela foi inspirada em lojas que possuem net e gross, além de controle de estoque simples


The Shop Application

funcionar com gate independente, o conceito de qrcodes tb pode ser usado para vendas de produtos e retirada no local,

explicar uso em excursoes, falar dos metafields na compra do produto

lista de convidados
ingressos manuais, isso devia estar no gate


ROADMAP



*************
CONTRIBUINDO
*************

Falar sobre gerar os .po antes de cada commit



*************
Documentation
*************

The documenation is written in rst format. It's available on the folder *docs/*. To write or read it in realtime install the sphinx dependencies using::

    $ python -m pip install docs/requirements.txt

And then execute the docs server via the command below::

    $ make docs

Your browser will open the local docs website (Running on port 8000 by default).


*********
Thanks to
*********

Project structure, documentation generation and other stuff from these
python boilerplate package projects:

* https://github.com/fabiommendes/python-boilerplate
* https://github.com/mtchavez/python-package-boilerplate
