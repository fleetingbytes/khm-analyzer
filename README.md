# khm-analyzer

## KHM

KHM is the common abbreviation for Kinder- und Hausmärchen which is the German title of Grimm's Fairy Tales. The fairy tales exist in many editions which can be downloaded from Deutches Textarchiv (DTA).

### Source Texts

First edition: [KHM vol. 1][khm-1-1], [KHM vol. 2][khm-2-1]

## Purpose

This tool helps to analyze the different editions of the fairy tales. It uses the linguistically annotated XML format provided by DTA.

## Development

### Dependencies

khm_analyzer uses [lxml][lxml] to parse XML. To be able to build the lxml dependency on FreeBSD you will need _libxml2_ and _libxslt_ installed on the system.
For formatting, this project uses [ruff][ruff]. To build ruff, you will need cmake installed on the system.

[khm-1-1]: https://deutschestextarchiv.de/book/show/grimm_maerchen01_1812
[khm-2-1]: https://deutschestextarchiv.de/book/show/grimm_maerchen02_1815
[lxml]: https://lxml.de
[ruff]: https://astral-sh/ruff
