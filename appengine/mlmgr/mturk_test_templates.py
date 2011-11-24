MASTER_TEST="""<QuestionForm xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd">
    <Overview>
        <Title>ISannounces Qualification Master Test</Title>
        <Text>
            Welcome to the ISannounces Qualification Master Test! First of all, thank you for taking time to look at our
            HITs and to take this qualification test.
        </Text>
        <Text>
            ISannounces is a great experiment in decision making which pursue two goals. The first one is to identify
            the optimal representation of information which enables a user to retrieve it with minimum efforts. We try
            to identify to which extend hierarchical categories, ontologies or tags can support users in retrieving
            specific information. The second one is to develop and train an artificial intelligence agent which is able
            to structure unstructured information, for example by assigning specific tags or categories to a body of
            text.
        </Text>
        <Text>
            In order to be able to validate our research hypotheses, we need to collect some demographic information.
            This information will be used to compare the results between various demographic groups. Our results should
            be consistent between these demographic groups.
        </Text>
        <Text>
            Your answers to this test will have NO EFFECT on your ability to perform our tasks or on your remuneration
            (inclusive bonus if applicable). As stated above, the goal of this test is only to collect demographic data
            to support our hypotheses.
        </Text>
    </Overview>
    <Question>
        <QuestionIdentifier>country_of_residence</QuestionIdentifier>
        <DisplayName>Country of Residence</DisplayName>
        <IsRequired>true</IsRequired>
        <QuestionContent>
            <Text>
                What is your current country of residence?
            </Text>
        </QuestionContent>
        <AnswerSpecification>
            <SelectionAnswer>
                <StyleSuggestion>dropdown</StyleSuggestion>
                <Selections>
                    <Selection><SelectionIdentifier>AF</SelectionIdentifier><Text>Afghanistan</Text></Selection>
                    <Selection><SelectionIdentifier>AL</SelectionIdentifier><Text>Albania</Text></Selection>
                    <Selection><SelectionIdentifier>DZ</SelectionIdentifier><Text>Algeria</Text></Selection>
                    <Selection><SelectionIdentifier>AS</SelectionIdentifier><Text>American Samoa</Text></Selection>
                    <Selection><SelectionIdentifier>AD</SelectionIdentifier><Text>Andorra</Text></Selection>
                    <Selection><SelectionIdentifier>AO</SelectionIdentifier><Text>Angola</Text></Selection>
                    <Selection><SelectionIdentifier>AI</SelectionIdentifier><Text>Anguilla</Text></Selection>
                    <Selection><SelectionIdentifier>AQ</SelectionIdentifier><Text>Antarctica</Text></Selection>
                    <Selection><SelectionIdentifier>AG</SelectionIdentifier><Text>Antigua And Barbuda</Text></Selection>
                    <Selection><SelectionIdentifier>AR</SelectionIdentifier><Text>Argentina</Text></Selection>
                    <Selection><SelectionIdentifier>AM</SelectionIdentifier><Text>Armenia</Text></Selection>
                    <Selection><SelectionIdentifier>AW</SelectionIdentifier><Text>Aruba</Text></Selection>
                    <Selection><SelectionIdentifier>AU</SelectionIdentifier><Text>Australia</Text></Selection>
                    <Selection><SelectionIdentifier>AT</SelectionIdentifier><Text>Austria</Text></Selection>
                    <Selection><SelectionIdentifier>AZ</SelectionIdentifier><Text>Azerbaijan</Text></Selection>
                    <Selection><SelectionIdentifier>BS</SelectionIdentifier><Text>Bahamas</Text></Selection>
                    <Selection><SelectionIdentifier>BH</SelectionIdentifier><Text>Bahrain</Text></Selection>
                    <Selection><SelectionIdentifier>BD</SelectionIdentifier><Text>Bangladesh</Text></Selection>
                    <Selection><SelectionIdentifier>BB</SelectionIdentifier><Text>Barbados</Text></Selection>
                    <Selection><SelectionIdentifier>BY</SelectionIdentifier><Text>Belarus</Text></Selection>
                    <Selection><SelectionIdentifier>BE</SelectionIdentifier><Text>Belgium</Text></Selection>
                    <Selection><SelectionIdentifier>BZ</SelectionIdentifier><Text>Belize</Text></Selection>
                    <Selection><SelectionIdentifier>BJ</SelectionIdentifier><Text>Benin</Text></Selection>
                    <Selection><SelectionIdentifier>BM</SelectionIdentifier><Text>Bermuda</Text></Selection>
                    <Selection><SelectionIdentifier>BT</SelectionIdentifier><Text>Bhutan</Text></Selection>
                    <Selection><SelectionIdentifier>BO</SelectionIdentifier><Text>Bolivia</Text></Selection>
                    <Selection><SelectionIdentifier>BA</SelectionIdentifier><Text>Bosnia And Herzegovina</Text></Selection>
                    <Selection><SelectionIdentifier>BW</SelectionIdentifier><Text>Botswana</Text></Selection>
                    <Selection><SelectionIdentifier>BV</SelectionIdentifier><Text>Bouvet Island</Text></Selection>
                    <Selection><SelectionIdentifier>BR</SelectionIdentifier><Text>Brazil</Text></Selection>
                    <Selection><SelectionIdentifier>IO</SelectionIdentifier><Text>British Indian Ocean Territory</Text></Selection>
                    <Selection><SelectionIdentifier>BN</SelectionIdentifier><Text>Brunei Darussalam</Text></Selection>
                    <Selection><SelectionIdentifier>BG</SelectionIdentifier><Text>Bulgaria</Text></Selection>
                    <Selection><SelectionIdentifier>BF</SelectionIdentifier><Text>Burkina Faso</Text></Selection>
                    <Selection><SelectionIdentifier>BI</SelectionIdentifier><Text>Burundi</Text></Selection>
                    <Selection><SelectionIdentifier>KH</SelectionIdentifier><Text>Cambodia</Text></Selection>
                    <Selection><SelectionIdentifier>CM</SelectionIdentifier><Text>Cameroon</Text></Selection>
                    <Selection><SelectionIdentifier>CA</SelectionIdentifier><Text>Canada</Text></Selection>
                    <Selection><SelectionIdentifier>CV</SelectionIdentifier><Text>Cape Verde</Text></Selection>
                    <Selection><SelectionIdentifier>KY</SelectionIdentifier><Text>Cayman Islands</Text></Selection>
                    <Selection><SelectionIdentifier>CF</SelectionIdentifier><Text>Central African Republic</Text></Selection>
                    <Selection><SelectionIdentifier>TD</SelectionIdentifier><Text>Chad</Text></Selection>
                    <Selection><SelectionIdentifier>CL</SelectionIdentifier><Text>Chile</Text></Selection>
                    <Selection><SelectionIdentifier>CN</SelectionIdentifier><Text>China</Text></Selection>
                    <Selection><SelectionIdentifier>CX</SelectionIdentifier><Text>Christmas Island</Text></Selection>
                    <Selection><SelectionIdentifier>CC</SelectionIdentifier><Text>Cocos (keeling) Islands</Text></Selection>
                    <Selection><SelectionIdentifier>CO</SelectionIdentifier><Text>Colombia</Text></Selection>
                    <Selection><SelectionIdentifier>KM</SelectionIdentifier><Text>Comoros</Text></Selection>
                    <Selection><SelectionIdentifier>CG</SelectionIdentifier><Text>Congo</Text></Selection>
                    <Selection><SelectionIdentifier>CD</SelectionIdentifier><Text>Congo (The Democratic Republic Of The)</Text></Selection>
                    <Selection><SelectionIdentifier>CK</SelectionIdentifier><Text>Cook Islands</Text></Selection>
                    <Selection><SelectionIdentifier>CR</SelectionIdentifier><Text>Costa Rica</Text></Selection>
                    <Selection><SelectionIdentifier>CI</SelectionIdentifier><Text>Cote D'ivoire</Text></Selection>
                    <Selection><SelectionIdentifier>HR</SelectionIdentifier><Text>Croatia</Text></Selection>
                    <Selection><SelectionIdentifier>CU</SelectionIdentifier><Text>Cuba</Text></Selection>
                    <Selection><SelectionIdentifier>CY</SelectionIdentifier><Text>Cyprus</Text></Selection>
                    <Selection><SelectionIdentifier>CZ</SelectionIdentifier><Text>Czech Republic</Text></Selection>
                    <Selection><SelectionIdentifier>DK</SelectionIdentifier><Text>Denmark</Text></Selection>
                    <Selection><SelectionIdentifier>DJ</SelectionIdentifier><Text>Djibouti</Text></Selection>
                    <Selection><SelectionIdentifier>DM</SelectionIdentifier><Text>Dominica</Text></Selection>
                    <Selection><SelectionIdentifier>DO</SelectionIdentifier><Text>Dominican Republic</Text></Selection>
                    <Selection><SelectionIdentifier>TP</SelectionIdentifier><Text>East Timor</Text></Selection>
                    <Selection><SelectionIdentifier>EC</SelectionIdentifier><Text>Ecuador</Text></Selection>
                    <Selection><SelectionIdentifier>EG</SelectionIdentifier><Text>Egypt</Text></Selection>
                    <Selection><SelectionIdentifier>SV</SelectionIdentifier><Text>El Salvador</Text></Selection>
                    <Selection><SelectionIdentifier>GQ</SelectionIdentifier><Text>Equatorial Guinea</Text></Selection>
                    <Selection><SelectionIdentifier>ER</SelectionIdentifier><Text>Eritrea</Text></Selection>
                    <Selection><SelectionIdentifier>EE</SelectionIdentifier><Text>Estonia</Text></Selection>
                    <Selection><SelectionIdentifier>ET</SelectionIdentifier><Text>Ethiopia</Text></Selection>
                    <Selection><SelectionIdentifier>FK</SelectionIdentifier><Text>Falkland Islands (malvinas)</Text></Selection>
                    <Selection><SelectionIdentifier>FO</SelectionIdentifier><Text>Faroe Islands</Text></Selection>
                    <Selection><SelectionIdentifier>FJ</SelectionIdentifier><Text>Fiji</Text></Selection>
                    <Selection><SelectionIdentifier>FI</SelectionIdentifier><Text>Finland</Text></Selection>
                    <Selection><SelectionIdentifier>FR</SelectionIdentifier><Text>France</Text></Selection>
                    <Selection><SelectionIdentifier>GF</SelectionIdentifier><Text>French Guiana</Text></Selection>
                    <Selection><SelectionIdentifier>PF</SelectionIdentifier><Text>French Polynesia</Text></Selection>
                    <Selection><SelectionIdentifier>TF</SelectionIdentifier><Text>French Southern Territories</Text></Selection>
                    <Selection><SelectionIdentifier>GA</SelectionIdentifier><Text>Gabon</Text></Selection>
                    <Selection><SelectionIdentifier>GM</SelectionIdentifier><Text>Gambia</Text></Selection>
                    <Selection><SelectionIdentifier>GE</SelectionIdentifier><Text>Georgia</Text></Selection>
                    <Selection><SelectionIdentifier>DE</SelectionIdentifier><Text>Germany</Text></Selection>
                    <Selection><SelectionIdentifier>GH</SelectionIdentifier><Text>Ghana</Text></Selection>
                    <Selection><SelectionIdentifier>GI</SelectionIdentifier><Text>Gibraltar</Text></Selection>
                    <Selection><SelectionIdentifier>GR</SelectionIdentifier><Text>Greece</Text></Selection>
                    <Selection><SelectionIdentifier>GL</SelectionIdentifier><Text>Greenland</Text></Selection>
                    <Selection><SelectionIdentifier>GD</SelectionIdentifier><Text>Grenada</Text></Selection>
                    <Selection><SelectionIdentifier>GP</SelectionIdentifier><Text>Guadeloupe</Text></Selection>
                    <Selection><SelectionIdentifier>GU</SelectionIdentifier><Text>Guam</Text></Selection>
                    <Selection><SelectionIdentifier>GT</SelectionIdentifier><Text>Guatemala</Text></Selection>
                    <Selection><SelectionIdentifier>GN</SelectionIdentifier><Text>Guinea</Text></Selection>
                    <Selection><SelectionIdentifier>GW</SelectionIdentifier><Text>Guinea-bissau</Text></Selection>
                    <Selection><SelectionIdentifier>GY</SelectionIdentifier><Text>Guyana</Text></Selection>
                    <Selection><SelectionIdentifier>HT</SelectionIdentifier><Text>Haiti</Text></Selection>
                    <Selection><SelectionIdentifier>HM</SelectionIdentifier><Text>Heard Island And Mcdonald Islands</Text></Selection>
                    <Selection><SelectionIdentifier>VA</SelectionIdentifier><Text>Holy See (vatican City State)</Text></Selection>
                    <Selection><SelectionIdentifier>HN</SelectionIdentifier><Text>Honduras</Text></Selection>
                    <Selection><SelectionIdentifier>HK</SelectionIdentifier><Text>Hong Kong</Text></Selection>
                    <Selection><SelectionIdentifier>HU</SelectionIdentifier><Text>Hungary</Text></Selection>
                    <Selection><SelectionIdentifier>IS</SelectionIdentifier><Text>Iceland</Text></Selection>
                    <Selection><SelectionIdentifier>IN</SelectionIdentifier><Text>India</Text></Selection>
                    <Selection><SelectionIdentifier>ID</SelectionIdentifier><Text>Indonesia</Text></Selection>
                    <Selection><SelectionIdentifier>IR</SelectionIdentifier><Text>Iran (Islamic Republic Of)</Text></Selection>
                    <Selection><SelectionIdentifier>IQ</SelectionIdentifier><Text>Iraq</Text></Selection>
                    <Selection><SelectionIdentifier>IE</SelectionIdentifier><Text>Ireland</Text></Selection>
                    <Selection><SelectionIdentifier>IL</SelectionIdentifier><Text>Israel</Text></Selection>
                    <Selection><SelectionIdentifier>IT</SelectionIdentifier><Text>Italy</Text></Selection>
                    <Selection><SelectionIdentifier>JM</SelectionIdentifier><Text>Jamaica</Text></Selection>
                    <Selection><SelectionIdentifier>JP</SelectionIdentifier><Text>Japan</Text></Selection>
                    <Selection><SelectionIdentifier>JO</SelectionIdentifier><Text>Jordan</Text></Selection>
                    <Selection><SelectionIdentifier>KZ</SelectionIdentifier><Text>Kazakstan</Text></Selection>
                    <Selection><SelectionIdentifier>KE</SelectionIdentifier><Text>Kenya</Text></Selection>
                    <Selection><SelectionIdentifier>KI</SelectionIdentifier><Text>Kiribati</Text></Selection>
                    <Selection><SelectionIdentifier>KP</SelectionIdentifier><Text>Korea (Democratic People's Republic Of)</Text></Selection>
                    <Selection><SelectionIdentifier>KR</SelectionIdentifier><Text>Korea (Republic Of)</Text></Selection>
                    <Selection><SelectionIdentifier>KV</SelectionIdentifier><Text>Kosovo</Text></Selection>
                    <Selection><SelectionIdentifier>KW</SelectionIdentifier><Text>Kuwait</Text></Selection>
                    <Selection><SelectionIdentifier>KG</SelectionIdentifier><Text>Kyrgyzstan</Text></Selection>
                    <Selection><SelectionIdentifier>LA</SelectionIdentifier><Text>Lao People's Democratic Republic</Text></Selection>
                    <Selection><SelectionIdentifier>LV</SelectionIdentifier><Text>Latvia</Text></Selection>
                    <Selection><SelectionIdentifier>LB</SelectionIdentifier><Text>Lebanon</Text></Selection>
                    <Selection><SelectionIdentifier>LS</SelectionIdentifier><Text>Lesotho</Text></Selection>
                    <Selection><SelectionIdentifier>LR</SelectionIdentifier><Text>Liberia</Text></Selection>
                    <Selection><SelectionIdentifier>LY</SelectionIdentifier><Text>Libyan Arab Jamahiriya</Text></Selection>
                    <Selection><SelectionIdentifier>LI</SelectionIdentifier><Text>Liechtenstein</Text></Selection>
                    <Selection><SelectionIdentifier>LT</SelectionIdentifier><Text>Lithuania</Text></Selection>
                    <Selection><SelectionIdentifier>LU</SelectionIdentifier><Text>Luxembourg</Text></Selection>
                    <Selection><SelectionIdentifier>MO</SelectionIdentifier><Text>Macau</Text></Selection>
                    <Selection><SelectionIdentifier>MK</SelectionIdentifier><Text>Macedonia (The Former Yugoslav Republic Of)</Text></Selection>
                    <Selection><SelectionIdentifier>MG</SelectionIdentifier><Text>Madagascar</Text></Selection>
                    <Selection><SelectionIdentifier>MW</SelectionIdentifier><Text>Malawi</Text></Selection>
                    <Selection><SelectionIdentifier>MY</SelectionIdentifier><Text>Malaysia</Text></Selection>
                    <Selection><SelectionIdentifier>MV</SelectionIdentifier><Text>Maldives</Text></Selection>
                    <Selection><SelectionIdentifier>ML</SelectionIdentifier><Text>Mali</Text></Selection>
                    <Selection><SelectionIdentifier>MT</SelectionIdentifier><Text>Malta</Text></Selection>
                    <Selection><SelectionIdentifier>MH</SelectionIdentifier><Text>Marshall Islands</Text></Selection>
                    <Selection><SelectionIdentifier>MQ</SelectionIdentifier><Text>Martinique</Text></Selection>
                    <Selection><SelectionIdentifier>MR</SelectionIdentifier><Text>Mauritania</Text></Selection>
                    <Selection><SelectionIdentifier>MU</SelectionIdentifier><Text>Mauritius</Text></Selection>
                    <Selection><SelectionIdentifier>YT</SelectionIdentifier><Text>Mayotte</Text></Selection>
                    <Selection><SelectionIdentifier>MX</SelectionIdentifier><Text>Mexico</Text></Selection>
                    <Selection><SelectionIdentifier>FM</SelectionIdentifier><Text>Micronesia (Federated States Of)</Text></Selection>
                    <Selection><SelectionIdentifier>MD</SelectionIdentifier><Text>Moldova (Republic Of)</Text></Selection>
                    <Selection><SelectionIdentifier>MC</SelectionIdentifier><Text>Monaco</Text></Selection>
                    <Selection><SelectionIdentifier>MN</SelectionIdentifier><Text>Mongolia</Text></Selection>
                    <Selection><SelectionIdentifier>MS</SelectionIdentifier><Text>Montserrat</Text></Selection>
                    <Selection><SelectionIdentifier>ME</SelectionIdentifier><Text>Montenegro</Text></Selection>
                    <Selection><SelectionIdentifier>MA</SelectionIdentifier><Text>Morocco</Text></Selection>
                    <Selection><SelectionIdentifier>MZ</SelectionIdentifier><Text>Mozambique</Text></Selection>
                    <Selection><SelectionIdentifier>MM</SelectionIdentifier><Text>Myanmar</Text></Selection>
                    <Selection><SelectionIdentifier>NA</SelectionIdentifier><Text>Namibia</Text></Selection>
                    <Selection><SelectionIdentifier>NR</SelectionIdentifier><Text>Nauru</Text></Selection>
                    <Selection><SelectionIdentifier>NP</SelectionIdentifier><Text>Nepal</Text></Selection>
                    <Selection><SelectionIdentifier>NL</SelectionIdentifier><Text>Netherlands</Text></Selection>
                    <Selection><SelectionIdentifier>AN</SelectionIdentifier><Text>Netherlands Antilles</Text></Selection>
                    <Selection><SelectionIdentifier>NC</SelectionIdentifier><Text>New Caledonia</Text></Selection>
                    <Selection><SelectionIdentifier>NZ</SelectionIdentifier><Text>New Zealand</Text></Selection>
                    <Selection><SelectionIdentifier>NI</SelectionIdentifier><Text>Nicaragua</Text></Selection>
                    <Selection><SelectionIdentifier>NE</SelectionIdentifier><Text>Niger</Text></Selection>
                    <Selection><SelectionIdentifier>NG</SelectionIdentifier><Text>Nigeria</Text></Selection>
                    <Selection><SelectionIdentifier>NU</SelectionIdentifier><Text>Niue</Text></Selection>
                    <Selection><SelectionIdentifier>NF</SelectionIdentifier><Text>Norfolk Island</Text></Selection>
                    <Selection><SelectionIdentifier>MP</SelectionIdentifier><Text>Northern Mariana Islands</Text></Selection>
                    <Selection><SelectionIdentifier>NO</SelectionIdentifier><Text>Norway</Text></Selection>
                    <Selection><SelectionIdentifier>OM</SelectionIdentifier><Text>Oman</Text></Selection>
                    <Selection><SelectionIdentifier>PK</SelectionIdentifier><Text>Pakistan</Text></Selection>
                    <Selection><SelectionIdentifier>PW</SelectionIdentifier><Text>Palau</Text></Selection>
                    <Selection><SelectionIdentifier>PS</SelectionIdentifier><Text>Palestinian Territory (Occupied)</Text></Selection>
                    <Selection><SelectionIdentifier>PA</SelectionIdentifier><Text>Panama</Text></Selection>
                    <Selection><SelectionIdentifier>PG</SelectionIdentifier><Text>Papua New Guinea</Text></Selection>
                    <Selection><SelectionIdentifier>PY</SelectionIdentifier><Text>Paraguay</Text></Selection>
                    <Selection><SelectionIdentifier>PE</SelectionIdentifier><Text>Peru</Text></Selection>
                    <Selection><SelectionIdentifier>PH</SelectionIdentifier><Text>Philippines</Text></Selection>
                    <Selection><SelectionIdentifier>PN</SelectionIdentifier><Text>Pitcairn</Text></Selection>
                    <Selection><SelectionIdentifier>PL</SelectionIdentifier><Text>Poland</Text></Selection>
                    <Selection><SelectionIdentifier>PT</SelectionIdentifier><Text>Portugal</Text></Selection>
                    <Selection><SelectionIdentifier>PR</SelectionIdentifier><Text>Puerto Rico</Text></Selection>
                    <Selection><SelectionIdentifier>QA</SelectionIdentifier><Text>Qatar</Text></Selection>
                    <Selection><SelectionIdentifier>RE</SelectionIdentifier><Text>Reunion</Text></Selection>
                    <Selection><SelectionIdentifier>RO</SelectionIdentifier><Text>Romania</Text></Selection>
                    <Selection><SelectionIdentifier>RU</SelectionIdentifier><Text>Russian Federation</Text></Selection>
                    <Selection><SelectionIdentifier>RW</SelectionIdentifier><Text>Rwanda</Text></Selection>
                    <Selection><SelectionIdentifier>SH</SelectionIdentifier><Text>Saint Helena</Text></Selection>
                    <Selection><SelectionIdentifier>KN</SelectionIdentifier><Text>Saint Kitts And Nevis</Text></Selection>
                    <Selection><SelectionIdentifier>LC</SelectionIdentifier><Text>Saint Lucia</Text></Selection>
                    <Selection><SelectionIdentifier>PM</SelectionIdentifier><Text>Saint Pierre And Miquelon</Text></Selection>
                    <Selection><SelectionIdentifier>VC</SelectionIdentifier><Text>Saint Vincent And The Grenadines</Text></Selection>
                    <Selection><SelectionIdentifier>WS</SelectionIdentifier><Text>Samoa</Text></Selection>
                    <Selection><SelectionIdentifier>SM</SelectionIdentifier><Text>San Marino</Text></Selection>
                    <Selection><SelectionIdentifier>ST</SelectionIdentifier><Text>Sao Tome And Principe</Text></Selection>
                    <Selection><SelectionIdentifier>SA</SelectionIdentifier><Text>Saudi Arabia</Text></Selection>
                    <Selection><SelectionIdentifier>SN</SelectionIdentifier><Text>Senegal</Text></Selection>
                    <Selection><SelectionIdentifier>RS</SelectionIdentifier><Text>Serbia</Text></Selection>
                    <Selection><SelectionIdentifier>SC</SelectionIdentifier><Text>Seychelles</Text></Selection>
                    <Selection><SelectionIdentifier>SL</SelectionIdentifier><Text>Sierra Leone</Text></Selection>
                    <Selection><SelectionIdentifier>SG</SelectionIdentifier><Text>Singapore</Text></Selection>
                    <Selection><SelectionIdentifier>SK</SelectionIdentifier><Text>Slovakia</Text></Selection>
                    <Selection><SelectionIdentifier>SI</SelectionIdentifier><Text>Slovenia</Text></Selection>
                    <Selection><SelectionIdentifier>SB</SelectionIdentifier><Text>Solomon Islands</Text></Selection>
                    <Selection><SelectionIdentifier>SO</SelectionIdentifier><Text>Somalia</Text></Selection>
                    <Selection><SelectionIdentifier>ZA</SelectionIdentifier><Text>South Africa</Text></Selection>
                    <Selection><SelectionIdentifier>GS</SelectionIdentifier><Text>South Georgia And The South Sandwich Islands</Text></Selection>
                    <Selection><SelectionIdentifier>ES</SelectionIdentifier><Text>Spain</Text></Selection>
                    <Selection><SelectionIdentifier>LK</SelectionIdentifier><Text>Sri Lanka</Text></Selection>
                    <Selection><SelectionIdentifier>SD</SelectionIdentifier><Text>Sudan</Text></Selection>
                    <Selection><SelectionIdentifier>SR</SelectionIdentifier><Text>Suriname</Text></Selection>
                    <Selection><SelectionIdentifier>SJ</SelectionIdentifier><Text>Svalbard And Jan Mayen</Text></Selection>
                    <Selection><SelectionIdentifier>SZ</SelectionIdentifier><Text>Swaziland</Text></Selection>
                    <Selection><SelectionIdentifier>SE</SelectionIdentifier><Text>Sweden</Text></Selection>
                    <Selection><SelectionIdentifier>CH</SelectionIdentifier><Text>Switzerland</Text></Selection>
                    <Selection><SelectionIdentifier>SY</SelectionIdentifier><Text>Syrian Arab Republic</Text></Selection>
                    <Selection><SelectionIdentifier>TW</SelectionIdentifier><Text>Taiwan (Province Of China)</Text></Selection>
                    <Selection><SelectionIdentifier>TJ</SelectionIdentifier><Text>Tajikistan</Text></Selection>
                    <Selection><SelectionIdentifier>TZ</SelectionIdentifier><Text>Tanzania (United Republic Of)</Text></Selection>
                    <Selection><SelectionIdentifier>TH</SelectionIdentifier><Text>Thailand</Text></Selection>
                    <Selection><SelectionIdentifier>TG</SelectionIdentifier><Text>Togo</Text></Selection>
                    <Selection><SelectionIdentifier>TK</SelectionIdentifier><Text>Tokelau</Text></Selection>
                    <Selection><SelectionIdentifier>TO</SelectionIdentifier><Text>Tonga</Text></Selection>
                    <Selection><SelectionIdentifier>TT</SelectionIdentifier><Text>Trinidad And Tobago</Text></Selection>
                    <Selection><SelectionIdentifier>TN</SelectionIdentifier><Text>Tunisia</Text></Selection>
                    <Selection><SelectionIdentifier>TR</SelectionIdentifier><Text>Turkey</Text></Selection>
                    <Selection><SelectionIdentifier>TM</SelectionIdentifier><Text>Turkmenistan</Text></Selection>
                    <Selection><SelectionIdentifier>TC</SelectionIdentifier><Text>Turks And Caicos Islands</Text></Selection>
                    <Selection><SelectionIdentifier>TV</SelectionIdentifier><Text>Tuvalu</Text></Selection>
                    <Selection><SelectionIdentifier>UG</SelectionIdentifier><Text>Uganda</Text></Selection>
                    <Selection><SelectionIdentifier>UA</SelectionIdentifier><Text>Ukraine</Text></Selection>
                    <Selection><SelectionIdentifier>AE</SelectionIdentifier><Text>United Arab Emirates</Text></Selection>
                    <Selection><SelectionIdentifier>GB</SelectionIdentifier><Text>United Kingdom</Text></Selection>
                    <Selection><SelectionIdentifier>US</SelectionIdentifier><Text>United States</Text></Selection>
                    <Selection><SelectionIdentifier>UM</SelectionIdentifier><Text>United States Minor Outlying Islands</Text></Selection>
                    <Selection><SelectionIdentifier>UY</SelectionIdentifier><Text>Uruguay</Text></Selection>
                    <Selection><SelectionIdentifier>UZ</SelectionIdentifier><Text>Uzbekistan</Text></Selection>
                    <Selection><SelectionIdentifier>VU</SelectionIdentifier><Text>Vanuatu</Text></Selection>
                    <Selection><SelectionIdentifier>VE</SelectionIdentifier><Text>Venezuela</Text></Selection>
                    <Selection><SelectionIdentifier>VN</SelectionIdentifier><Text>Viet Nam</Text></Selection>
                    <Selection><SelectionIdentifier>VG</SelectionIdentifier><Text>Virgin Islands (British)</Text></Selection>
                    <Selection><SelectionIdentifier>VI</SelectionIdentifier><Text>Virgin Islands (U.S.)</Text></Selection>
                    <Selection><SelectionIdentifier>WF</SelectionIdentifier><Text>Wallis And Futuna</Text></Selection>
                    <Selection><SelectionIdentifier>EH</SelectionIdentifier><Text>Western Sahara</Text></Selection>
                    <Selection><SelectionIdentifier>YE</SelectionIdentifier><Text>Yemen</Text></Selection>
                    <Selection><SelectionIdentifier>ZM</SelectionIdentifier><Text>Zambia</Text></Selection>
                    <Selection><SelectionIdentifier>ZW</SelectionIdentifier><Text>Zimbabwe</Text></Selection>
                </Selections>
            </SelectionAnswer>
        </AnswerSpecification>
    </Question>
    <Question>
        <QuestionIdentifier>gender</QuestionIdentifier>
        <DisplayName>Gender</DisplayName>
        <IsRequired>true</IsRequired>
        <QuestionContent>
            <Text>
                What is your gender?
            </Text>
        </QuestionContent>
        <AnswerSpecification>
            <SelectionAnswer>
                <StyleSuggestion>radiobutton</StyleSuggestion>
                <Selections>
                    <Selection>
                        <SelectionIdentifier>male</SelectionIdentifier>
                        <Text>Male</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>female</SelectionIdentifier>
                        <Text>Female</Text>
                    </Selection>
                </Selections>
            </SelectionAnswer>
        </AnswerSpecification>
    </Question>
    <Question>
        <QuestionIdentifier>year_of_birth</QuestionIdentifier>
        <DisplayName>Year of Birth</DisplayName>
        <IsRequired>true</IsRequired>
        <QuestionContent>
            <Text>
                What is your 4 digits year of birth (eg. 1971)?
            </Text>
        </QuestionContent>
        <AnswerSpecification>
            <FreeTextAnswer>
                <Constraints>
                    <AnswerFormatRegex regex="^[12][0-9]{3}$"
                                       errorText="You must enter a year with the format yyyy (eg. 1971)."/>
                </Constraints>
            </FreeTextAnswer>
        </AnswerSpecification>
    </Question>
    <Question>
        <QuestionIdentifier>education</QuestionIdentifier>
        <DisplayName>Education</DisplayName>
        <IsRequired>true</IsRequired>
        <QuestionContent>
            <Text>
                What is your higher educational level?
            </Text>
        </QuestionContent>
        <AnswerSpecification>
            <SelectionAnswer>
                <StyleSuggestion>radiobutton</StyleSuggestion>
                <Selections>
                    <Selection>
                        <SelectionIdentifier>some_high_school</SelectionIdentifier>
                        <Text>Some High School</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>high_school_graduate</SelectionIdentifier>
                        <Text>High School Graduate</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>some_college</SelectionIdentifier>
                        <Text>Some College, no Degree</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>associates_degree</SelectionIdentifier>
                        <Text>Associates Degree</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>bachelors_degree</SelectionIdentifier>
                        <Text>Bachelors Degree</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>masters_degree</SelectionIdentifier>
                        <Text>Graduate Degree, Master</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>doctorate_degree</SelectionIdentifier>
                        <Text>Graduate Degree, Doctorate</Text>
                    </Selection>
                </Selections>
            </SelectionAnswer>
        </AnswerSpecification>
    </Question>
    <Question>
        <QuestionIdentifier>prior_knowledge</QuestionIdentifier>
        <DisplayName>Prior Knowledge</DisplayName>
        <IsRequired>true</IsRequired>
        <QuestionContent>
            <Text>
                Did you have some prior knowledge of the followings?
            </Text>
        </QuestionContent>
        <AnswerSpecification>
            <SelectionAnswer>
                <StyleSuggestion>checkbox</StyleSuggestion>
                <Selections>
                    <Selection>
                        <SelectionIdentifier>job_postings</SelectionIdentifier>
                        <Text>Job postings (reading, searching, ...)</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>cfp</SelectionIdentifier>
                        <Text>Academic conferences calls for papers</Text>
                    </Selection>
                    <Selection>
                        <SelectionIdentifier>academia</SelectionIdentifier>
                        <Text>Academic conferences and journals</Text>
                    </Selection>
                </Selections>
            </SelectionAnswer>
        </AnswerSpecification>
    </Question>
    <Overview>
        <Text>
            Your are already done! Thanks for taking time to complete our Qualification Master Test. To reward the time
            spent, you will receive a $0.10 bonus when completing your first HIT with us.
        </Text>
    </Overview>
</QuestionForm>"""