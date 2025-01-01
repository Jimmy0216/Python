import requests

# 네이버 API 키 설정
client_id = 'mz2ndtwfhe'  # 네이버 클라우드 플랫폼에서 발급받은 클라이언트 ID
client_secret = 'p4l9fh2s86SOJxksMPXFnqRquyJENsVLfY7TvgUK'  # 네이버 클라우드 플랫폼에서 발급받은 클라이언트 시크릿

# 장소 이름
place_name = '서울특별시 노원구 롯데시네마'

# 네이버 Geocoding API 호출 함수 정의
def geocode_place(place_name):
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={place_name}"
    headers = {
        'X-NCP-APIGW-API-KEY-ID': client_id,
        'X-NCP-APIGW-API-KEY': client_secret
    }
    response = requests.get(url, headers=headers)
    
    # 응답 상태 코드 확인
    if response.status_code == 200:
        data = response.json()
        print(data)  # API 응답 출력
        if data['addresses']:
            location = data['addresses'][0]
            return location['y'], location['x']
        else:
            print("주소를 찾을 수 없습니다.")
            return None, None
    else:
        # 에러 메시지 출력
        print(f"Error {response.status_code}: {response.text}")
        return None, None

# 장소 이름을 좌표로 변환
latitude, longitude = geocode_place(place_name)

# 결과 출력
if latitude and longitude:
    print(f"장소: {place_name}")
    print(f"위도: {latitude}")
    print(f"경도: {longitude}")
else:
    print("좌표를 찾을 수 없습니다.")