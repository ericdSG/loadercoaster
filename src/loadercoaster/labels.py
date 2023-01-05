class Label:
    def __init__(self, *args, **kwargs) -> None:
        self.id = None
        self.dimension = None
        self.data = None

    def __len__(self) -> int:
        raise NotImplementedError


class Audio(Label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sample_rate = None
        self.state = None

    def __len__(self) -> int:
        pass


class CarnivalRTS(Label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.frame_rate = None
        self.channels = None

    def __len__(self) -> int:
        pass


class CarnivalSEG(Label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.labels = None

    def __len__(self) -> int:
        pass


class String(Label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __len__(self) -> int:
        pass


class Custom(Label):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __len__(self) -> int:
        pass
