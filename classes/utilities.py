class Utilities:

    def get_input() -> list:
        ret = []
        with open("input.txt", "r") as f:
            for x in f.read().splitlines():
                ret.append(x.split())
        return ret
