import streamlit as st
import openai
import json

library_regulations = """
   제1장 총칙

 제1조(목적) 이 규정은 「대학도서관진흥법」과 「국립부경대학교 학칙」(이하 “학칙”이라 한다) 제11조의3에 따라 국립부경대학교 도서관(이하 “도서관”이라 한다)의 발전계획 수립과 진행, 직원의 배치, 학술정보자료의 확보와 효율적인 이용 및 관리에 관한 사항을 규정함을 목적으로 한다.

 제2조(임무) 도서관은 대학교육의 목적달성을 위하여 국내외 각종 정보자료(이하 “자료”라 한다)를 수집, 정리, 보존하여 교직원, 학생 및 지역주민들의 연구, 학습에 제공함을 임무로 한다.

       제2장 조직

 제3조(조직) ① 학칙 제11조의3제1항에 따라 임명된 도서관장(이하 “관장”이라 한다)의 임기는 2년으로 하되 연임할 수 있다.

② 관장은 도서관 운영에 관한 모든 업무를 총괄한다.

③ 학칙 제10조의5에 따라 설치된 학술정보지원실에는 팀을 두어 운용하며, 팀 조직에 관한 사항은 관장이 별도로 정한다.  <개정 2022. 8. 22.>

 제4조(도서관 운영위원회) 도서관에서는 도서관 운영위원회(이하 “위원회”라 한다)를 두며, 위원회의 구성과 운영에 관한 사항은 따로 정한다.

       제3장 도서관 발전계획

 제5조(발전계획의 수립) ① 관장은 「대학도서관진흥법」 제8조의 종합계획에 기초하여 5년마다 발전계획 개시 연도의 2월 말일까지 다음 각 호의 사항이 포함된 발전계획을 수립한다.

1. 도서관 발전의 기본방향 및 목표

2. 도서관 자료 개발 및 확충 방안

3. 도서관 시설 및 환경 개선 방안

4. 도서관 이용자에 대한 서비스 활성화 방안

5. 도서관 인적 자원의 개발 및 관리 방안

6. 그 밖에 도서관 발전을 위하여 필요한 사항

② 관장은 다음 각 호의 사항이 포함된 도서관 발전 연도별 시행계획(이하 “연도별계획”이라 한다)을 매년 2월말까지 수립한다.

1. 전년도 연도별계획의 시행 결과

2. 해당 연도의 도서관 발전사업 추진 방향

3. 도서관 관련 주요 사업별 추진방향 및 세부 운영계획

       제4장 직원의 배치 및 교육

 제6조(직원의 배치) ① 총장은 도서관에 「대학도서관진흥법」 및 같은 법 시행령에서 정한 기준 이상의 사서를 두어야 하고, 필요한 경우 전산직원 등 전문 직원을 둘 수 있다.

② 관장은 대학의 교육·연구 지원을 위한 충분한 사서 및 전문 직원을 확보·배치하도록 노력하여야 한다.

 제7조(교육 훈련) 도서관에 근무하는 사서 및 전문 직원은 업무 수행 능력 향상을 위하여 「대학도서관진흥법」에서 제시한 연간 최소 교육시간 이상의 교육·훈련을 이수하여야 한다.

       제5장 자료의 수집 및 관리

 제8조(자료 구입 예산 및 소장) ① 관장은 도서관에 교수 연구와 학생 학습을 위한 충분한 도서관 자료를 확충할 수 있도록 예산을 확보한다.

② 관장은 「대학도서관진흥법」 및 같은 법 시행령에서 정한 도서관 자료기준 기본도서는 학생 1인당 70권 이상, 연간 증가 도서 수는 학생 1인당 2권 이상을 확보하도록 노력하여야 한다.

 제9조(자료의 구분) 자료는 다음 각 호와 같이 구분한다.

1. 단행본

2. 연속간행물

3. 참고자료

4. 전자자료

5. 비도서자료

6. 학위논문

7. 귀중자료

8. 기타자료

 제10조(수집자료의 구분) 도서관이 수집하는 자료는 다음 각 호와 같이 구분한다.

1. 구입자료

2. 수증자료

3. 교환자료

4. 편입자료

 제11조(자료관리의 범위) 도서관이 관리하는 자료는 다음 각 호와 같다.

1. 도서관에 소장하고 있는 자료

2. 도서관 자료로서 교내 각 기관에 비치하고 있는 자료

 제12조(자료의 선정 및 구입) ① 자료의 균형적 발전을 기하고 장서의 일관성 있는 수준을 유지할 수 있도록 다음 각호를 참고하여 자료를 선정한다.

1. 교수의 학술연구 및 교육에 필요한 자료

2. 학생의 학습 및 교양에 필요한 자료

3. 그 밖에 관장이 필요하다고 인정하는 자료

② 도서관은 자료의 질, 이용자의 요구, 예산 등을 고려하여 구입하는 자료의 수량을 조정할 수 있다.

 제13조(자료의 납본) 교내에서 발간되는 자료는 발행일로부터 30일 이내에 2부를 도서관에 납본하여야 한다.

 제14조(자료의 등록 및 정리) ① 구입 자료는 등록함을 원칙으로 하고, 수증·교환·편입 자료는 도서관 장서로서 가치가 있다고 인정되는 자료를 등록한다.

② 도서관에 등록된 자료의 정리에 관한 사항은 관장이 별도로 정한다.

 제15조(문고설치) ① 개인 및 단체로부터 기증받은 자료는 문고를 설치할 수 있다.

② 수증자료의 관리와 기증(기부)자에 대한 예우는 관장이 별도로 정한다. <개정 2023.10.16.>

 제16조(자료의 폐기 및 제적) 도서관이 소장한 자료는 「도서관법」에 정한 범위에서 폐기 및 제적할 수 있다.

       제6장 시설 및 자료의 이용

 제17조(시설에 관한 기준) 관장은 학생 수, 장서 수 등을 고려하여 재학생 1인당 1.2제곱미터 이상의 연면적 시설을 확보하여야 한다.

 제18조(자격) 다음 각 호에 해당하는 사람은 도서관이 소장하고 있는 자료 및 시설을 이용할 수 있으며 이용 범위는 관장이 별도로 정한다.

1. 교직원 및 재학생

2. 관장의 허가를 받은 그 밖의 사람

 제19조(개관 시간) 도서관의 개관 시간은 관장이 별도로 정한다.

 제20조(휴관일) 도서관의 휴관일은 다음 각 호와 같다. 다만, 관장은 필요에 따라 이를 조정할 수 있다.

1. 자료실: 공휴일, 개교기념일

2. 일반열람실: 설날, 추석

 제21조(자료대출) 제18조에 규정된 사람은 본인의 신분증으로 대출할 수 있다.

 제22조(대출책수 및 기간) ① 단행본 대출 책 수 및 기간은 다음 각 호와 같다.

1. 전임교원, 겸임교원, 명예교수, 강사: 50책 이내 90일

2. 직원, 조교, 대학원생: 20책 이내 30일

3. 학부생: 10책 이내 14일<개정 2023.10.16.>

② 제1항에 명시된 모든 사람들에 대한 전자책 대출 책 수는 5책 이내로 하며, 대출 기간은 5일로 하되, 연구원 및 도서관회원에게도 동일하게 적용한다. <개정 2023.10.16.>

③ 그 밖의 대출 책 수 및 기간에 관한 사항은 관장이 별도로 정한다.

 제23조(대출 제한 자료) 다음 각 호의 자료는 대출할 수 없다. 다만, 관장이 필요하다고 인정할 때 단기간 대출을 허가할 수 있다.

1. 연속간행물

2. 참고자료

3. 학위논문

4. 귀중자료

5. 비도서자료

6. 관장이 지정한 그 밖의 자료

 제24조(대출기간 중 반납) ① 다음 각 호의 사유 발생 시에는 대출받은 자료를 즉시 반납하여야 한다.

1. 휴직, 정직, 전출, 퇴직, 정학, 퇴학, 제적, 수료, 졸업 등

2. 자료의 운용상 필요하여 관장의 요구가 있을 때

② 졸업이나 수료 예정자는 학위수여일 30일 전부터 대출이 중지되고, 대출 자료를 반납하여야 한다.

 제25조(관내수칙) 도서관 이용자는 자료 보존 및 면학분위기 조성을 위하여 다음 각 호의 행위를 하여서는 아니 된다.

1. 자료 또는 물품의 훼손 및 무단 반출

2. 신분증을 대여하거나 무단 사용

3. 지정된 장소 외에서 식음이나 흡연

4. 지정된 장소 외의 게시물 부착

5. 인쇄물 및 그 밖의 물품 배포

6. 다른 이용자에게 방해가 되는 그 밖의 행위

 제26조(개인정보 및 인권보호) 관장은 「개인정보 보호법」에 따른 이용자의 개인정보 및 인권을 보호하여야 한다.

       제7장 비치자료

 제27조(비치 자료) 도서관은 교내 각 기관에 다음 각 호의 자료를 비치할 수 있다.

1. 교내 각 기관에서 수집하여 등록 및 정리절차를 마친 자료

2. 도서관에 2책 이상 소장하는 자료로서 다른 전문분야와 공통되지 아니하는 자료

 제28조(비치 절차) 교내 각 기관장이 자료를 비치하고자 할 때에는 관장의 허가를 얻어 비치할 수 있다.

 제29조(관리 및 책임) ① 교내 각 기관에 비치한 자료에 대하여는 해당 기관의 장이 관리 보관할 책임을 진다.

② 비치한 자료는 그 목록을 작성 보관하여야 하며, 오손 기타 이상이 있을 때는 즉시 그 사유를 관장에게 통보하여야 한다.

 제30조(비치 자료의 반납) 비치 자료로서 이용할 필요가 없게 된 때는 즉시 반납하여야 하며, 관장은 관리상 필요에 따라 점검 및 반납을 요구할 수 있다.

       제8장 보칙

 제31조(운영세칙 등) 도서관 운영에 필요한 세부사항은 위원회의 심의를 거쳐 관장이 별도로 정한다.

       제9장 제재

 제32조(자료대출 중지) ① 대출한 자료를 기한 내에 반납하지 아니하면 다른 자료 대출 및 도서관 이용을 중지한다.

② 대출 중지 및 면제방법은 관장이 별도로 정한다.

 제33조(자료의 변상) ① 자료를 분실 또는 훼손하였을 경우에는 도서관에 신고하고 신고일로부터 10일 이내에 동일자료로 변상하여야 한다.

② 동일 자료의 변상이 불가능할 경우 변상방법은 관장이 별도로 정한다.

 제34조(자료반납 불이행자에 대한 조치) 관장은 자료를 기한 내에 반납하지 않은 이용자에 대하여 본인 또는 해당 부서장에게 다음 각 호의 조치를 요청할 수 있다.

1. 각종 증명서 발급 보류

2. 장학금 지급 및 휴학 등 승인 보류

 제35조(질서 위반자에 대한 조치) ①관장은 도서관의 시설과 자료를 이용함에 있어 타인에게 불편을 초래하거나 도서관규정 및 세칙을 위반한 사람에게 도서관 이용 중지 등의 제재를 취할 수 있다.

② 질서유지를 위한 처분기준은 관장이 별도로 정한다.


부칙 <제38호,1996.8.16.> 조문목록 없음  부      칙 <제38호, 1996.8.16.>

제1조(시행일) 이 규정은 공포한 날부터 시행한다.

부칙 <제254호,2001.11.1.> 조문목록 없음  부      칙 <제254호, 2001.11.1.>

제1조 (시행일) 이 규정은 공포한 날부터 시행한다.

부칙 <제637호,2010.8.5.> 조문목록 없음  부      칙 <제637호, 2010.8.5.>

제1조 (시행일) 이 규정은 공포한 날부터 시행한다.

부칙 <제641호,2010.9.15.> 조문목록 접기  부      칙 <제641호, 2010.9.15.>

제1조(시행일) 이 규정은 공포한 날부터 시행한다.

제2조(폐지규정) 이 규정의 시행으로 종전의 “부경대학교출판부규정”은 폐지한다.

부칙 <제934호,2017.5.29.> 조문목록 없음  부      칙 <제934호, 2017.5.29.>

 이 규정은 공포한 날부터 시행한다.

부칙 <제1034호,2019.8.1.>(부경대학교 학칙)  조문목록 접기  부      칙 <제1034호, 2019.8.1.>(부경대학교 학칙)

제1조(시행일) 이 학칙은 공포한 날부터 시행한다. 다만 제5조, 제7조제1항, 제17조제1항 및 부칙 제2조의 개정학칙은 2019년 8월 1일부터 시행하며, 별표 1 및 별표 6의 개정학칙은 2020년 3월 1일부터 시행한다.

제2조(전공명칭 변경에 따른 경과조치) 이 학칙 시행으로 “자원·정보경제학전공” 소속학생은 “자원환경경제학전공” 소속 학생으로 본다.

제3조(다른 규정의 개정) ① 「부경대학교 캠퍼스기획위원회 규정」 일부를 다음과 같이 개정한다.

제3조제3항 중 “재직교원”을 “전임교원”으로 한다.

② 「부경대학교 연구소(센터) 설립 및 폐지에 관한 규정」 일부를 다음과 같이 개정한다.

제4조제3항제2호 중 “교원”을 “전임교원”으로 한다.

③ 「부경대학교 표창 규정」 일부를 다음과 같이 개정한다.

제3조제2호 중 “교직원”을 “전임교원 및 직원”으로 한다.

④ 「부경대학교 대학회계 재정 및 회계의 운영에 관한 규정」 일부를 다음과 같이 개정한다.

제4조제3항, 제5조제1호, 제6조제1항제1호 중 “교원”을 “전임교원”으로, 제12조제1항, 제12조제2항 중 “교직원”을 “전임교원, 공무원조교, 공무원직원, 대학회계 호봉제적용 정규직원”으로 한다.

⑤ 「부경대학교 학사학위과정 운영 규정」 일부를 다음과 같이 개정한다.

제21조 중 “시간강사”를 “강사”로, 제46조제3항제4호 중 “교원”을 “전임교원”으로 한다.

⑥ 「부경대학교 등록금심의위원회 규정」 일부를 다음과 같이 개정한다.

제3조제2항 중 “교직원”을 “전임교원 및 직원”으로 한다.

⑦ 「부경대학교 동물실험윤리위원회 운영 규정」 일부를 다음과 같이 개정한다.

제4조제4호, 제8조제1항 중 “교원”을 “전임교원”으로 한다.

⑧ 「부경대학교 신산학융합본부 인재개발원 규정」 일부를 다음과 같이 개정한다.

제3조제2항, 제10조제1항, 제15조제1항, 제17조제1항 중 “교직원”을 “전임교원 및 직원”으로 한다.

⑨ 「부경대학교 입학전형관리위원회 규정」 일부를 다음과 같이 개정한다.

제5조제2항 중 “교직원”을 “전임교원 및 직원”로 한다.

⑩ 「부경대학교 도서관 규정」 일부를 다음과 같이 개정한다.

제22조제1호 중 “교원”을 “전임교원”으로, 제22조제2호 중 “직원, 조교, 대학원생”을 “직원, 조교, 대학원생, 겸임교원 등 및 강사”로 한다.

⑪ 「부경대학교 학생상담센터 규정」 일부를 다음과 같이 개정한다.제12조 중 “교직원”을 “전임교원, 조교 및 직원”으로 한다.

⑫ 「부경대학교 생활관비심의위원회 규정」 일부를 다음과 같이 개정한다.

제3조제1항 중 “교직원”을 “전임교원 및 직원”으로, 제3조제2항 중 “교직원”을 “전임교원”으로 한다.

⑬ 「부경대학교 부경언론사 규정」 일부를 다음과 같이 개정한다.

제8조제1항, 제16조제2항 중 “교원”을 “전임교원”으로 한다.

⑭ 「부경대학교 링크플러스 사업단 운영 규정」 일부를 다음과 같이 개정한다.

제8조제2항, 제16조제2항, 제16조제3항, 제27조제2항 중 “교원”을 “전임교원”으로 한다.

⑮ 「부경대학교 해양탐구교육원 규정」 일부를 다음과 같이 개정한다.

제4조제1항 중 “교원”을 “전임교원”으로 한다.

부칙 <제1124호,2021.2.1.> 조문목록 접기  부      칙 <제1124호, 2021.2.1.>

제1조(시행일) 이 학칙은 공포한 날부터 시행한다. 다만 제65조제2항은 2010학년도 이후 학번의 재적생부터 적용한다.

제2조(다른규정의 개정) ① 「부경대학교 도서관 규정」 일부를 다음과 같이 개정한다.

제3조제3항 중 “학술정보과”를 “학술정보원”으로 한다.

 ② 「부경대학교 대학도서관운영위원회 규정」 일부를 다음과 같이 개정한다.

제6조 제1항 중 “학술정보과”를 “학술정보원”으로 한다.

 ③ 「부경대학교 현장실습 운영 규정」 일부를 다음과 같이 개정한다.

제3조 제1항 중 “인재개발원”을 “학생역량개발과”로 한다.

 ④ 「부경대학교 대학일자리센터 규정」 일부를 다음과 같이 개정한다.

제3조  중 “신산학융합본부”를 “학생처”로, 제5조 중 “신산학융합본부장”을 “학생처장”, “인재개발원장”을 “학생역량개발부처장”으로, 제7조 중 “인재개발원장, 신산학개발원장”을 “학생역량개발부처장”으로 한다.

 ⑤ 「부경대학교 기록관 운영규정」 일부를 다음과 같이 개정한다.

제4조 제1항 중 “기록관에 관장을 두며, 기록관장은 본교 교수 또는 부교수 중에서 총장이 임명한다.”를 “기록관은 총무과 소속으로 하며, 기록관의 장은 총무과장이 된다.”로 하며 제7조를 삭제한다.

 ⑥ 「부경대학교 교육과정운영위원회 규정」 일부를 다음과 같이 개정한다.

제2조 제3항 중 “학생부처장”을 “학생역량개발부처장”으로 하고, “인재개발원장”을 삭제하며, 제5항 중 “학생역량개발원장”을 “학생역량개발부처장”, “교수학습성과원장”을 “교수학습지원센터장”, “기획부처장”을 “성과관리센터장”으로 하고, “학생부처장”을 삭제하며, 제6항 중 “학생역량개발원장”을 “학생역량개발부처장”, “교수학습성과원장”을 “교수학습지원센터장”, “기획부처장”을 “성과관리센터장”으로 하고 “학생부처장”을 삭제한다.

 ⑦ 「부경대학교 링크플러스 사업단 운영규정」 일부를 다음과 같이 개정한다.

제7조 제6항 중 “인재개발원장”을 “학생역량개발부처장”으로 한다.

 ⑧ 「부경대학교 비교과교육과정 운영 규정」 일부를 다음과 같이 개정한다. 제2조제3호 중 “미래교육혁신본부 학생역량개발원”을 “학생역량개발과”로 한다.

 ⑨ 「부경대학교 보안업무 시행 규정」 일부를 다음과 같이 개정한다.

제2조  중 “미래교육혁신본부”를 삭제하고 “부속시설”을 “학부대학, 부속시설”로 하며, 제4조제3항제3호의 “기획과장”을 “기획전략과장”으로 한다.

 ⑩ 「부경대학교 연구비 감사 규정」 일부를 다음과 같이 개정한다.

제4조 제2항의 “산학부총장”을 “대외부총장”으로 한다.

⑪ 「부경대학교 기획위원회 규정」 일부를 다음과 같이 개정한다.

제8조제2항 중 “기획팀장”을 “기획전략과 팀장”으로 한다.

⑫ 「부경대학교 캠퍼스기획위원회 규정」 일부를 다음과 같이 개정한다.

제3조제2항 중 “기획과장”을 “기획전략과장”으로, 제6조제2항 중 “캠퍼스평가팀장”을 “기획전략과 팀장” 으로 한다.

 ⑬ 「부경대학교 대학자체평가 등에 관한 규정」 일부를 다음과 같이 개정한다.

제8조 제3항 중 “기획과장”을 “기획전략과장”으로 한다.

 ⑭ 「부경대학교 제 규정 관리 규정」 일부를 다음과 같이 개정한다.

제8조 제4항 중 “기획과장”을 “기획전략과장”으로 한다.

 ⑮ 「부경대학교 드래곤밸리지원센터 규정」을 「부경대학교 기업지원컨택센터 규정」으로 하고 일부를 다음과 같이 개정한다.

제1조  및 제2조 중 “드래곤밸리지원센터”를 “기업지원컨택센터”로 한다.

 ? 「부경대학교 재정지원사업성과관리센터 운영 규정」 일부를 다음과 같이 개정한다.

제1조  및 제2조의 “재정지원사업성과관리센터”를 “성과관리센터”로, 제2조제2호 중 “성과 평가”를 “성과 분석·평가”로, 제2조제3호 중 “재정지원사업의”를 삭제하며, 제3조제3항 중 “기획과”를 “기획전략과”로, 제7조 중“자체평가위원회 및”을 “자체평가위원회,”로, “사업중복방지위원회”를 “사업중복방지위원회 및 교육성과 분석·관리를 위한 교육성과관리위원회”로 한다.

 ? 「부경대학교 다문화 및 북한이탈 학생 지원에 관한 규정」 일부를 다음과 같이 개정한다.

제4조 제1항제3호 중 “인재개발원”을 “학생역량개발과”로 한다.

 ? 「부경대학교 신산학융합본부 신산학개발원 규정」 일부를 다음과 같이 개정한다.

제3조 제1항 중 “부교수 이상의”를 “조교수 이상의”로 하고, 제4항 중 “부교수 이상의”를 “조교수 이상의”로 한다.

제3조(다른규정의 폐지) 「부경대학교 신산학융합본부 인재개발원 규정」, 「부경대학교 미래교육혁신본부 운영 규정」, 「부경대학교 체육부운영위원회 규정」, 「부경대학교 체육진흥관리위원회 규정」, 「부경대학교 생활체육지도자연수원 운영 규정」은 이를 폐지한다.

부칙 <제1165호,2021.5.31.> 조문목록 없음  부      칙 <제1165호, 2021.5.31.>

 이 규정은 공포한 날부터 시행한다.

부칙 <제1237호,2022.7.12.> 조문목록 없음  부      칙 <제1237호, 2022.7.12.>

 이 규정은 공포한 날부터 시행한다.

부칙 <제1307호,2023.10.16.> 조문목록 없음  부      칙 <제1307호, 2023.10.16.>

 이 규정은 공포한 날부터 시행한다.

부칙 <제1316호,2023.12.27.> 조문목록 접기  부      칙 <제1316호, 2023.12.27.>

제1조(시행일) 이 학칙은 공포한 날로부터 시행한다. 다만, “별표 2”의 “수산물리학과”, “별표 3”, “별표 5”의 융합전공 폐지는 2024년 3월 1일부터 적용하며, “별표 2”의 “에너지융합소재공학과”는 2024년 9월 1일부터 적용한다.

제2조(대학원 모집단위 변경에 따른 경과조치) 이 학칙 시행으로 일반대학원(석사과정 및 박사과정)의 “수산물리학과” 재적생은 “해양생산관리학부 수산물리학전공” 재적생으로 본다.

제3조(글로벌정책대학원 모집단위 변경에 따른 경과조치) 이 학칙 시행으로 폐지된 “일본학과” 재적생은 졸업 시까지 동 전공에 재적하는 것으로 본다.

제4조(다른 규정의 개정) 본교 제 규정의 제명 및 내용 중 “부경대학교”는 “국립부경대학교”로 한다.
"""

st.title("국립부경대학교 도서관 규정 Q&A")


def show_message(msg):
    if msg['role'] == 'user' or msg['role'] == 'assistant':
        with st.chat_message(msg['role']):
            st.markdown(msg["content"])

# Initialization

client = st.session_state.get('openai_client', None)
if client is None:
    if st.button("API Key를 입력하세요."):
        st.switch_page("pages/1_Setting.py")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "assistant" not in st.session_state:
    st.session_state.assistant = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "다음은 국립부경대학교 도서관 규정입니다:"},
            {"role": "system", "content": library_regulations},
        ],
    )


if "thread" not in st.session_state:
    st.session_state.thread = client.beta.threads.create()


# Page

st.header("Chat")

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear (Start a new chat)"):
        st.session_state.messages = []
        del st.session_state.thread
with col2:
    if st.button("Leave"):
        st.session_state.messages = []
        del st.session_state.thread
        del st.session_state.assistant

# previous chat
for msg in st.session_state.messages:
    show_message(msg)

# user prompt, assistant response
if prompt := st.chat_input("도서관 규정에 대한 질문을 입력하세요."):
    msg = {"role":"user", "content":prompt}
    show_message(msg)
    st.session_state.messages.append(msg)

    # assistant api - get response
    thread = st.session_state.thread
    assistant = st.session_state.assistant

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    while run.status == 'requires_action':
        tool_calls = run.required_action.submit_tool_outputs.tool_calls
        tool_outputs = []
        for tool in tool_calls:
            func_name = tool.function.name
            kwargs = json.loads(tool.function.arguments)
            output = None
            if func_name in TOOL_FUNCTIONS:
                output = TOOL_FUNCTIONS[func_name](**kwargs)
            tool_outputs.append(
                {
                    "tool_call_id": tool.id,
                    "output": str(output)
                }
            )
        run = client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
            
    # assistant messages - text, image_url, image_file
    if run.status == 'completed':
        api_response = client.beta.threads.messages.list(
            thread_id=thread.id,
            run_id=run.id,
            order="asc"
        )
        for data in api_response.data:
            for content in data.content:
                if content.type == 'text':
                    response = content.text.value
                    msg = {"role":"assistant","content":response}
                show_message(msg)
                st.session_state.messages.append(msg)

