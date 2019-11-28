import portpicker



if __name__ == '__main__':
    test_port = portpicker.is_port_free(55555)
    print(test_port)
