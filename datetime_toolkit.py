from calendar import day_name, month_name, weekday
from datetime import datetime
from locale import LC_ALL, setlocale
from time import time

from ntplib import NTPClient
from pytz import country_names, country_timezones, timezone


class DatetimeToolkit:
    delta_server = None

    def __init__(self, ntp = 'ntp.shoa.cl', tz = 'America/Santiago', locale = None):
        """Class to work with NTP servers, time zones, localized names of months and weekdays.
        The default parameters are from Chile. The "locale" parameter is set to None by default to avoid errors with
        languages that are not installed on the system.

        :param ntp: NTP server URL/IP to be used.
        :param tz: Time zone code to be used by "pytz" library.
        :param locale: Localization code to be used for months and weekdays names."""
        self._ntp_server_url = ntp
        self._client = NTPClient()
        self._tz = timezone(tz)
        self._tz_utc = timezone('UTC')
        self.server_time()  # Updating delta_server

        self._locale = locale
        if locale is not None:
            setlocale(LC_ALL, locale)
        self.days = list(map(self._first_letter_uppercase, day_name))
        self.months = list(map(self._first_letter_uppercase, month_name[1:]))

    @staticmethod
    def country_information(alpha_2_code: str) -> dict[str, list[str] | str]:
        """Method to find information about a country using its alpha-2 code.

        https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

        :param alpha_2_code: ISO 3166 alpha-2 code of the country.
        :return: Dictionary with country information. Keys are the strings "country" and "time_zones"."""
        return {'country': country_names[alpha_2_code], 'time_zones': country_timezones[alpha_2_code]}

    def locale(self) -> str | None:
        """:return: Locale used as string. None if no locale was provided."""
        return self._locale

    def server_url(self) -> str:
        """:return: NTP server URL/IP as string."""
        return self._ntp_server_url

    def tz(self) -> datetime.tzinfo:
        """:return: Object datetime.tzinfo for the given time zone."""
        return self._tz

    @staticmethod
    def local_time() -> float:
        """Wrapper of time.time()

        :return: Float timestamp of the current local time."""
        return time()

    def server_time(self) -> int:
        """NTP server time. This method updates delta_server property, which holds the difference between server time
        and local time.

        :return: Integer timestamp of the server time."""
        server_time = self._client.request(self._ntp_server_url).tx_time
        self.delta_server = server_time - self.local_time()
        return server_time

    def datetime(self, is_request_forced = False, is_utc = False) -> datetime:
        """It calculates the server timestamp using the delta_server property to avoid unnecessary requests to the NTP
        server. You can force the request to the server using the boolean parameter is_request_forced.

        :param is_request_forced: Boolean to query the server instead of calculating the server time from delta_server.
        :param is_utc: Replaces given time zone with UTC time zone.
        :return: Datetime object using time zone."""
        if is_request_forced:
            timestamp = self.server_time()
        else:
            timestamp = self.local_time() + self.delta_server
        time_zone = self._tz_utc if is_utc else self._tz
        return datetime.fromtimestamp(timestamp, time_zone)

    def string(self, is_request_forced = False, is_utc = False, string_format = '%Y-%m-%d %H:%M:%S') -> str:
        """It calculates the server timestamp using the delta_server property to avoid unnecessary requests to the NTP
        server. You can force the request to the server using the boolean parameter is_request_forced.

        :param is_request_forced: Boolean to query the server instead of calculating the server time from delta_server.
        :param is_utc: Replaces given time zone with UTC time zone.
        :param string_format: String format to be used by strftime method.
        :return: String representing datetime using string_format."""
        return self.datetime(is_request_forced = is_request_forced, is_utc = is_utc).strftime(string_format)

    def float_to_datetime(self, timestamp: float, is_utc = False) -> datetime:
        """:param timestamp: Float timestamp to be converted to datetime.
        :param is_utc: Replaces given time zone with UTC time zone.
        :return: Datetime from timestamp using time zone."""
        time_zone = self._tz_utc if is_utc else self._tz
        return datetime.fromtimestamp(timestamp, time_zone)

    def float_to_string(self, timestamp: float, is_utc = False, string_format = '%Y-%m-%d %H:%M:%S') -> str:
        """:param timestamp: Float timestamp to be converted to formatted string.
        :param is_utc: Replaces given time zone with UTC time zone.
        :param string_format: String format to be used by strftime method.
        :return: String from timestamp using given time zone and string_format."""
        return self.float_to_datetime(timestamp = timestamp, is_utc = is_utc).strftime(string_format)

    @staticmethod
    def _first_letter_uppercase(word: str) -> str:
        """:param word: String to be formatted.
        :return: String with the first letter uppercase and the rest lowercase."""
        return word[0].upper() + word[1:].lower()

    def name_month(self, custom_datetime: datetime = None, is_request_forced = False, is_utc = False) -> str:
        """:param custom_datetime: Datetime object to be used to find the name of the month.
        :param is_request_forced: Boolean to query the server instead of calculating the server time from delta_server.
        :param is_utc: Boolean to use given time zone or UTC time zone.
        :return: String of the localized month name."""
        if custom_datetime is None:
            now = self.datetime(is_request_forced = is_request_forced, is_utc = is_utc)
        else:
            now = custom_datetime
        return self.months[now.month - 1]  # Months start from 1

    def name_day(self, custom_datetime: datetime = None, is_request_forced = False, is_utc = False) -> str:
        """:param custom_datetime: Datetime object to be used to find the name of the day.
        :param is_request_forced: Boolean to query the server instead of calculating the server time from delta_server.
        :param is_utc: Boolean to use given time zone or UTC time zone.
        :return: String of the localized day name."""
        if custom_datetime is None:
            now = self.datetime(is_request_forced = is_request_forced, is_utc = is_utc)
        else:
            now = custom_datetime
        return self.days[weekday(year = now.year, month = now.month, day = now.day)]
