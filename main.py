class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str):
        """Инициализация социальной сети.

        Args:
            name: Название социальной сети.
        """
        self.name = name

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        pass

    def __repr__(self) -> str:
        """Представление объекта для внутреннего использования."""
        pass


class VK(SocialNetwork):
    """Дочерний класс для социальной сети VK."""

    def __init__(self, name: str, users: int):
        """Инициализация социальной сети VK.

        Args:
            name: Название социальной сети.
            users: Количество пользователей.
        """
        super().__init__(name)
        self.users = users

    def __str__(self) -> str:
        """Строковое представление объекта VK."""
        pass

    def __repr__(self) -> str:
        """Представление объекта VK для внутреннего использования."""
        pass

    def update_users(self, new_users: int) -> None:
        """Обновляет количество пользователей.

        Args:
            new_users: Новое количество пользователей.
        """
        pass

    def customize_profile(self) -> None:
        """Перегрузка метода customize_profile для VK.

        Метод customize_profile перегружается для VK, так как в VK могут быть уникальные настройки профиля,
        отличающиеся от базовой социальной сети.
        """
        pass


class Facebook(SocialNetwork):
    """Дочерний класс для социальной сети Facebook."""

    def __init__(self, name: str, groups: int):
        """Инициализация социальной сети Facebook.

        Args:
            name: Название социальной сети.
            groups: Количество групп.
        """
        super().__init__(name)
        self.groups = groups

    def __str__(self) -> str:
        """Строковое представление объекта Facebook."""
        pass

    def __repr__(self) -> str:
        """Представление объекта Facebook для внутреннего использования."""
        pass

    def post_to_groups(self, content: str) -> None:
        """Постит контент в группы.

        Args:
            content: Контент для публикации.
        """
        pass

    def like_post(self) -> None:
        """Перегрузка метода like_post для Facebook.

        Метод like_post перегружается для Facebook, так как способ лайка контента может отличаться
        от других социальных сетей.
        """
        pass
