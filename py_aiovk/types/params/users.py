from pydantic import BaseModel


class UsersGetFollowersParams(BaseModel):
    user_id: int = None
    offset: int = None
    count: int = None
    fields: str = None
    name_case: str = None


class UsersGetSubscriptionsParams(BaseModel):
    user_id: int = None
    extended: bool = None
    offset: int = None
    count: int = None
    fields: str = None


class UsersGetParams(BaseModel):
    user_ids: str = None
    fields: str = None
    name_case: str = None


class UsersSearchParams(BaseModel):
    q: str = None
    sort: int = None
    offset: int = None
    count: int = None
    fields: str = None
    city: int = None
    city_id: int = None
    country: int = None
    country_id: int = None
    hometown: str = None
    university_country: int = None
    university: int = None
    university_year: int = None
    university_faculty: int = None
    university_chair: int = None
    sex: int = None
    status: int = None
    age_from: int = None
    age_to: int = None
    birth_day: int = None
    birth_month: int = None
    birth_year: int = None
    online: bool = None
    has_photo: bool = None
    school_country: int = None
    school_city: int = None
    school_class: int = None
    school: int = None
    school_year: int = None
    religion: str = None
    company: str = None
    position: str = None
    group_id: int = None
    from_list: str = None
    screen_ref: str = None


