<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="https://github.com/svaldivia12/datetime_toolkit">
        <img src="https://github.com/svaldivia12/datetime_toolkit/raw/main/images/logo.png" alt="Logo" width="80" height="80">
        <h3 align="center">Datetime Toolkit</h3>
    </a>
    <p align="center">
        Python package to work with NTP servers, time zones, and localized names of months and days of the week.
        <br /><br />
        <a href="https://github.com/svaldivia12/datetime_toolkit/issues">Report Bug</a>
        ·
        <a href="https://github.com/svaldivia12/datetime_toolkit/issues">Request Feature</a>
    </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#🏁-getting-started">🏁 Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#✨-usage">✨ Usage</a></li>
        <ul>
            <li><a href="#default-instantation">Default instantation</a></li>
            <li><a href="#custom-instantation">Custom instantation</a></li>
            <li><a href="#class-datetimeToolkit-properties-and-methods">Class DatetimeToolkit properties and methods</a></li>
        </ul>
    <li><a href="#🤝🏼-contributing">🤝🏼 Contributing</a></li>
    <li><a href="#📜️️-license">📜️️ License</a></li>
    <li><a href="#📬-contact">📬 Contact</a></li>
    <li><a href="#🙏🏼-acknowledgments">🙏🏼 Acknowledgments</a></li>
  </ol>
</details>

<!-- GETTING STARTED -->
## 🏁 Getting Started
### Prerequisites
- Python 3

### Installation
Using `pip`
```sh
pip install datetime_toolkit
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## ✨ Usage
### Default instantation
Default parameters are from 🇨🇱 Chile:
- NTP Server: [ntp.shoa.cl](https://shoabucket.s3.amazonaws.com/horaoficial.cl/procedimiento/procedimiento_ntp.pdf)
- Time zone: America / Santiago
- Locale: **Your system default locale**

To use custom locale, the language must be installed on your system. On Linux, check your `/etc/locale.gen` file.
For example, I have English, Spanish and German installed.
```sh
grep -v "#" /etc/locale.gen

en_US.UTF-8 UTF-8
es_CL.UTF-8 UTF-8
de_DE.UTF-8 UTF-8
```
```python
datetime_toolkit = DatetimeToolkit(locale = 'es_CL.UTF-8')
print(datetime_toolkit.months)
print(datetime_toolkit.days)

# Printed values
['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
```

### Custom instantation
To use custom parameters, use the country [ISO 3166 alpha-2 code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) to find your country information.

For example, the country code for 🇩🇪 Germany is "DE", so you can use:

```python
info = DatetimeToolkit.country_information(alpha_2_code = 'de')

# Static method country_information(code) will return a dictionary like this
info = {'country': 'Germany', 'time_zones': ['Europe/Berlin', 'Europe/Busingen']}
```
I will use [PTB NTP server](https://www.ptb.de/cms/ptb/fachabteilungen/abtq/gruppe-q4/ref-q42/zeitsynchronisation-von-rechnern-mit-hilfe-des-network-time-protocol-ntp.html) (`ptbtime1.ptb.de`) and the timezone from Berlin.
```python
datetime_toolkit = DatetimeToolkit(ntp = 'ptbtime1.ptb.de', tz = 'Europe/Berlin', locale = 'de_DE.UTF-8')
print(datetime_toolkit.months)
print(datetime_toolkit.days)

# Printed values
['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
```
### Class DatetimeToolkit properties and methods

| **Property** | **Returns**                                                                                                                                                                  |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| days | List with the names of the days of the week as strings. Language used is determined by locale parameter or system default. First letter is uppercase and the rest lowercase. |
| months | List with the names of the months as strings. Language used is determined by locale parameter or system default. First letter is uppercase and the rest lowercase.           |


| **Method** | **Returns** |
|---|---|
| @staticmethod<br/>country_information(alpha_2_code: str) | Dictionary with country information. Keys are the strings "country" and "time_zones". |
| locale() | Locale used as string. None if no locale was provided. |
| server_url() | NTP server URL/IP as string. |
| tz() | Object datetime.tzinfo for the given time zone. |
| local_time() | Float timestamp of the current local time. Wrapper of time.time() |
| server_time() | Int timestamp of the server time. |
| datetime(is_request_forced = False, is_utc = False) | Datetime object using given time zone. |
| string(is_request_forced = False, is_utc = False, string_format = '%Y-%m-%d %H:%M:%S') | String representing datetime using string_format. |
| float_to_datetime(timestamp: float, is_utc = False) | Datetime from timestamp using given time zone. |
| float_to_string(timestamp: float, is_utc = False, string_format = '%Y-%m-%d %H:%M:%S') | String from timestamp using given time zone and string_format. |
| name_month(custom_datetime: datetime = None, is_request_forced = False, is_utc = False) | String of the localized month name. If custom_datetime is None, it will use datetime() method. |
| name_day(custom_datetime: datetime = None, is_request_forced = False, is_utc = False) | String of the localized day name. If custom_datetime is None, it will use datetime() method. |

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝🏼 Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## 📜️️ License
Distributed under the **MIT License**. See [`LICENSE.txt`][license-url] for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## 📬 Contact
👨🏻‍💻 Sebastián Valdivia Loyola [ [✉️ E-Mail](mailto:admin@svaldivia.cl) -  [📂 GitHub](https://github.com/svaldivia12) - [📦 Project](https://github.com/svaldivia12/datetime_toolkit) ]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## 🙏🏼 Acknowledgments
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/svaldivia12/datetime_toolkit.svg?style=for-the-badge
[contributors-url]: https://github.com/svaldivia12/datetime_toolkit/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/svaldivia12/datetime_toolkit.svg?style=for-the-badge
[forks-url]: https://github.com/svaldivia12/datetime_toolkit/network/members
[stars-shield]: https://img.shields.io/github/stars/svaldivia12/datetime_toolkit.svg?style=for-the-badge
[stars-url]: https://github.com/svaldivia12/datetime_toolkit/stargazers
[issues-shield]: https://img.shields.io/github/issues/svaldivia12/datetime_toolkit.svg?style=for-the-badge
[issues-url]: https://github.com/svaldivia12/datetime_toolkit/issues
[license-shield]: https://img.shields.io/github/license/svaldivia12/datetime_toolkit.svg?style=for-the-badge
[license-url]: https://github.com/svaldivia12/datetime_toolkit/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/sebastian-valdivia-loyola
