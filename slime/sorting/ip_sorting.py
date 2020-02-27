__doc__ = \
    """
    This module houses functions to sort an iterable of IP 
    addresses based on octet values. Subnet masks may be used in some
    only if the entire IP address is in CIDR notation. However, who uses 
    anything else these days? All of these functions use the built-in sorted
    function given a lambda function for the sorting key.
    """


def sort_ipv4_addresses_without_mask(ip_address_iterable):
    """
        Sort IPv4 addresses only

        | :param iter ip_address_iterable: An iterable container of IPv4 addresses
        | :return list : A sorted list of IPv4 addresses
        """
    return sorted(
        ip_address_iterable,
        key=lambda addr: (
            int(addr.split('.')[0]),
            int(addr.split('.')[1]),
            int(addr.split('.')[2]),
            int(addr.split('.')[3]),
        )
    )


def sort_ipv4_addresses_with_mask(ip_address_iterable):
    """
    Sort IPv4 addresses in CIDR notation

    | :param iter ip_address_iterable: An iterable container of IPv4 CIDR notated addresses
    | :return list : A sorted list of IPv4 CIDR notated addresses
    """
    return sorted(
        ip_address_iterable,
        key=lambda addr: (
            int(addr.split('.')[0]),
            int(addr.split('.')[1]),
            int(addr.split('.')[2]),
            int(addr.split('.')[3].split('/')[0]),
            int(addr.split('.')[3].split('/')[1])
        )
    )


def sort_ipv6_address_with_mask(ip_address_iterable):
    """
        Sort IPv6 addresses in CIDR notation

        | :param iter ip_address_iterable: An iterable container of IPv6 CIDR notated addresses
        | :return list : A sorted list of IPv6 CIDR notated addresses
        """
    return sorted(
        ip_address_iterable,
        key=lambda addr: (
            int(addr.split(':')[0]),
            int(addr.split(':')[1]),
            int(addr.split(':')[2]),
            int(addr.split(':')[3]),
            int(addr.split(':')[4]),
            int(addr.split(':')[5]),
            int(addr.split(':')[6]),
            int(addr.split(':')[7]),
            int(addr.split(':')[8]),
            int(addr.split(':')[9]),
            int(addr.split(':')[10]),
            int(addr.split(':')[11]),
            int(addr.split(':')[12]),
            int(addr.split(':')[13]),
            int(addr.split(':')[14]),
            int(addr.split(':')[15].split('/')[0]),
            int(addr.split(':')[15].split('/')[1]),
        )
    )


def sort_ipv6_address_without_mask(ip_address_iterable):
    """
        Sort IPv6 addresses

        | :param iter ip_address_iterable: An iterable container of IPv6 addresses
        | :return list : A sorted list of IPv6 addresses
        """
    return sorted(
        ip_address_iterable,
        key=lambda addr: (
            int(addr.split(':')[0]),
            int(addr.split(':')[1]),
            int(addr.split(':')[2]),
            int(addr.split(':')[3]),
            int(addr.split(':')[4]),
            int(addr.split(':')[5]),
            int(addr.split(':')[6]),
            int(addr.split(':')[7]),
            int(addr.split(':')[8]),
            int(addr.split(':')[9]),
            int(addr.split(':')[10]),
            int(addr.split(':')[11]),
            int(addr.split(':')[12]),
            int(addr.split(':')[13]),
            int(addr.split(':')[14]),
            int(addr.split(':')[15]),
        )
    )
