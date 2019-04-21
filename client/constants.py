class Period:
    """Periods available for the charts
    Values are the minutes of each period
    """
    m1 = 1
    m5 = 5
    m15 = 15
    m30 = 30
    h1 = 60  # 1 hour
    h4 = 240  # 4 hours
    d1 = 1440  # 1 day
    w1 = 10080  # 1 week
    mn1 = 43200  # 1 month


class ProfitMode:
    forex = 5
    cfd = 6

    descriptions = {
        forex: 'Forex',
        cfd: 'CFD'
    }


class MarginMode:
    forex = 101
    cfd_leveraged = 102
    cfd = 103

    descriptions = {
        forex: 'Forex',
        cfd_leveraged: 'CFD Leveraged',
        cfd: 'CFD'
    }
