from pydantic import BaseModel


class GroupsGetMembersParams(BaseModel):
    group_id: str = None
    sort: str = None
    offset: int = None
    count: int = None
    fields: str = None
    filter: str = None


class GroupsEditParams(BaseModel):
    group_id: int = None
    title: str = None
    description: str = None
    screen_name: str = None
    access: int = None
    website: str = None
    subject: int = None
    email: str = None
    phone: str = None
    rss: str = None
    event_start_date: int = None
    event_finish_date: int = None
    event_group_id: int = None
    public_category: int = None
    public_subcategory: int = None
    public_date: str = None
    wall: int = None
    topics: int = None
    photos: int = None
    video: int = None
    audio: int = None
    links: bool = None
    events: bool = None
    places: bool = None
    contacts: bool = None
    docs: int = None
    wiki: int = None
    messages: bool = None
    articles: bool = None
    addresses: bool = None
    age_limits: int = None
    market: bool = None
    market_buttons: str = None
    market_comments: bool = None
    market_country: str = None
    market_city: str = None
    market_currency: int = None
    market_contact: int = None
    market_wiki: int = None
    obscene_filter: bool = None
    obscene_stopwords: bool = None
    toxic_filter: bool = None
    disable_replies_from_groups: bool = None
    obscene_words: str = None
    main_section: int = None
    secondary_section: int = None
    country: int = None
    city: int = None


class GroupsIsMemberParams(BaseModel):
    group_id: str = None
    user_id: int = None
    user_ids: str = None
    extended: bool = None


class GroupsCreateParams(BaseModel):
    title: str = None
    description: str = None
    type: str = None
    public_category: int = None
    public_subcategory: int = None
    subtype: int = None


class GroupsGetInvitesParams(BaseModel):
    offset: int = None
    count: int = None
    extended: bool = None


class GroupsSearchParams(BaseModel):
    q: str = None
    type: str = None
    country_id: int = None
    city_id: int = None
    future: bool = None
    market: bool = None
    sort: int = None
    offset: int = None
    count: int = None


class GroupsApproveRequestParams(BaseModel):
    group_id: int = None
    user_id: int = None


class GroupsGetParams(BaseModel):
    user_id: int = None
    extended: bool = None
    filter: str = None
    fields: str = None
    offset: int = None
    count: int = None


class GroupsGetByIdParams(BaseModel):
    group_ids: str = None
    group_id: str = None
    fields: str = None


class GroupsGetAddressesParams(BaseModel):
    group_id: int = None
    address_ids: str = None
    latitude: str = None
    longitude: str = None
    offset: int = None
    count: int = None
    fields: str = None


class GroupsInviteParams(BaseModel):
    group_id: int = None
    user_id: int = None


class GroupsJoinParams(BaseModel):
    group_id: int = None
    not_sure: str = None


class GroupsLeaveParams(BaseModel):
    group_id: int = None


class GroupsRemoveUserParams(BaseModel):
    group_id: int = None
    user_id: int = None


