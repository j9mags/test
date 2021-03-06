# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 10:05
from __future__ import unicode_literals

from django.db import migrations
import salesforce.backend.operations
import salesforce.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, db_column='Id', primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', salesforce.fields.BooleanField(default=False, verbose_name='Deleted')),
                ('name', salesforce.fields.CharField(max_length=255, verbose_name='Account Name')),
                ('immatrikulationsnummer', salesforce.fields.CharField(blank=True, max_length=255, null=True)),
                ('unimailadresse', salesforce.fields.EmailField(blank=True, max_length=254, null=True)),
                ('studiengebuehren_gesamt', salesforce.fields.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Studiengebühren gesamt')),
                ('geschlecht', salesforce.fields.CharField(blank=True, choices=[('weiblich', 'weiblich'), ('männlich', 'männlich'), ('geschlechtsneutral', 'geschlechtsneutral')], max_length=255, null=True)),
                ('geburtsort', salesforce.fields.CharField(blank=True, max_length=255, null=True)),
                ('geburtsdatum', salesforce.fields.DateField(blank=True, null=True)),
                ('geburtsland', salesforce.fields.CharField(blank=True, choices=[('Abchasien', 'Abchasien'), ('Afghanistan', 'Afghanistan'), ('Ägypten', 'Ägypten'), ('Albanien', 'Albanien'), ('Algerien', 'Algerien'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua und Barbuda', 'Antigua und Barbuda'), ('Äquatorialguinea', 'Äquatorialguinea'), ('Argentinien', 'Argentinien'), ('Armenien', 'Armenien'), ('Aserbaidschan', 'Aserbaidschan'), ('Äthiopien', 'Äthiopien'), ('Australien', 'Australien'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesch', 'Bangladesch'), ('Barbados', 'Barbados'), ('Belgien', 'Belgien'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bergkarabach', 'Bergkarabach'), ('Bhutan', 'Bhutan'), ('Bolivien', 'Bolivien'), ('Bosnien und Herzegowina', 'Bosnien und Herzegowina'), ('Botswana', 'Botswana'), ('Brasilien', 'Brasilien'), ('Brunei', 'Brunei'), ('Bulgarien', 'Bulgarien'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Chile', 'Chile'), ('Republik China', 'Republik China'), ('Volksrepublik China', 'Volksrepublik China'), ('Cookinseln', 'Cookinseln'), ('Costa Rica', 'Costa Rica'), ('Dänemark', 'Dänemark'), ('Deutschland', 'Deutschland'), ('Dominica', 'Dominica'), ('Dominikanische Republik', 'Dominikanische Republik'), ('Dschibuti', 'Dschibuti'), ('Ecuador', 'Ecuador'), ('El Salvador', 'El Salvador'), ('Elfenbeinküste', 'Elfenbeinküste'), ('Eritrea', 'Eritrea'), ('Estland', 'Estland'), ('Fidschi', 'Fidschi'), ('Finnland', 'Finnland'), ('Frankreich', 'Frankreich'), ('Gabun', 'Gabun'), ('Gambia', 'Gambia'), ('Georgien', 'Georgien'), ('Ghana', 'Ghana'), ('Grenada', 'Grenada'), ('Griechenland', 'Griechenland'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Indien', 'Indien'), ('Indonesien', 'Indonesien'), ('Irak', 'Irak'), ('Iran', 'Iran'), ('Irland', 'Irland'), ('Island', 'Island'), ('Israel', 'Israel'), ('Italien', 'Italien'), ('Jamaika', 'Jamaika'), ('Japan', 'Japan'), ('Jemen', 'Jemen'), ('Jordanien', 'Jordanien'), ('Kambodscha', 'Kambodscha'), ('Kamerun', 'Kamerun'), ('Kanada', 'Kanada'), ('Kap Verde', 'Kap Verde'), ('Kasachstan', 'Kasachstan'), ('Katar', 'Katar'), ('Kenia', 'Kenia'), ('Kirgisistan', 'Kirgisistan'), ('Kiribati', 'Kiribati'), ('Kolumbien', 'Kolumbien'), ('Komoren', 'Komoren'), ('Kongo, Demokratische Republik', 'Kongo, Demokratische Republik'), ('Kongo, Republik', 'Kongo, Republik'), ('Korea, Nord', 'Korea, Nord'), ('Korea, Süd', 'Korea, Süd'), ('Kosovo', 'Kosovo'), ('Kroatien', 'Kroatien'), ('Kuba', 'Kuba'), ('Kuwait', 'Kuwait'), ('Laos', 'Laos'), ('Lesotho', 'Lesotho'), ('Lettland', 'Lettland'), ('Libanon', 'Libanon'), ('Liberia', 'Liberia'), ('Libyen', 'Libyen'), ('Liechtenstein', 'Liechtenstein'), ('Litauen', 'Litauen'), ('Luxemburg', 'Luxemburg'), ('Madagaskar', 'Madagaskar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Malediven', 'Malediven'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marokko', 'Marokko'), ('Marshallinseln', 'Marshallinseln'), ('Mauretanien', 'Mauretanien'), ('Mauritius', 'Mauritius'), ('Mazedonien', 'Mazedonien'), ('Mexiko', 'Mexiko'), ('Mikronesien', 'Mikronesien'), ('Moldawien', 'Moldawien'), ('Monaco', 'Monaco'), ('Mongolei', 'Mongolei'), ('Montenegro', 'Montenegro'), ('Mosambik', 'Mosambik'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Neuseeland', 'Neuseeland'), ('Nicaragua', 'Nicaragua'), ('Niederlande', 'Niederlande'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Nordzypern', 'Nordzypern'), ('Norwegen', 'Norwegen'), ('Oman', 'Oman'), ('Österreich', 'Österreich'), ('Osttimor / Timor-Leste', 'Osttimor / Timor-Leste'), ('Pakistan', 'Pakistan'), ('Palästina', 'Palästina'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua-Neuguinea', 'Papua-Neuguinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippinen', 'Philippinen'), ('Polen', 'Polen'), ('Portugal', 'Portugal'), ('Ruanda', 'Ruanda'), ('Rumänien', 'Rumänien'), ('Russland', 'Russland'), ('Salomonen', 'Salomonen'), ('Sambia', 'Sambia'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('São Tomé und Príncipe', 'São Tomé und Príncipe'), ('Saudi-Arabien', 'Saudi-Arabien'), ('Schweden', 'Schweden'), ('Schweiz', 'Schweiz'), ('Senegal', 'Senegal'), ('Serbien', 'Serbien'), ('Seychellen', 'Seychellen'), ('Sierra Leone', 'Sierra Leone'), ('Simbabwe', 'Simbabwe'), ('Singapur', 'Singapur'), ('Slowakei', 'Slowakei'), ('Slowenien', 'Slowenien'), ('Somalia', 'Somalia'), ('Somaliland', 'Somaliland'), ('Spanien', 'Spanien'), ('Sri Lanka', 'Sri Lanka'), ('St. Kitts und Nevis', 'St. Kitts und Nevis'), ('St. Lucia', 'St. Lucia'), ('St. Vincent und die Grenadinen', 'St. Vincent und die Grenadinen'), ('Südafrika', 'Südafrika'), ('Sudan', 'Sudan'), ('Südossetien', 'Südossetien'), ('Südsudan', 'Südsudan'), ('Suriname', 'Suriname'), ('Swasiland', 'Swasiland'), ('Syrien', 'Syrien'), ('Tadschikistan', 'Tadschikistan'), ('Tansania', 'Tansania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Transnistrien', 'Transnistrien'), ('Trinidad und Tobago', 'Trinidad und Tobago'), ('Tschad', 'Tschad'), ('Tschechien', 'Tschechien'), ('Tunesien', 'Tunesien'), ('Türkei', 'Türkei'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('Ungarn', 'Ungarn'), ('Uruguay', 'Uruguay'), ('Usbekistan', 'Usbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatikanstadt', 'Vatikanstadt'), ('Venezuela', 'Venezuela'), ('Vereinigte Arabische Emirate', 'Vereinigte Arabische Emirate'), ('Vereinigte Staaten', 'Vereinigte Staaten'), ('Vereinigtes Königreich', 'Vereinigtes Königreich'), ('Vietnam', 'Vietnam'), ('Weißrussland', 'Weißrussland'), ('Westsahara', 'Westsahara'), ('Zentral\xadafrikanische Republik', 'Zentral\xadafrikanische Republik'), ('Zypern', 'Zypern')], max_length=255, null=True)),
                ('staatsangehoerigkeit', salesforce.fields.CharField(blank=True, choices=[('afghanisch', 'afghanisch'), ('ägyptisch', 'ägyptisch'), ('albanisch', 'albanisch'), ('algerisch', 'algerisch'), ('andorranisch', 'andorranisch'), ('angolanisch', 'angolanisch'), ('antiguanisch', 'antiguanisch'), ('äquatorialguineisch', 'äquatorialguineisch'), ('argentinisch', 'argentinisch'), ('armenisch', 'armenisch'), ('aserbaidschanisch', 'aserbaidschanisch'), ('äthiopisch', 'äthiopisch'), ('australisch', 'australisch'), ('bahamaisch', 'bahamaisch'), ('bahrainisch', 'bahrainisch'), ('bangladeschisch', 'bangladeschisch'), ('barbadisch', 'barbadisch'), ('belgisch', 'belgisch'), ('belizisch', 'belizisch'), ('beninisch', 'beninisch'), ('bhutanisch', 'bhutanisch'), ('bolivianisch', 'bolivianisch'), ('bosnisch-herzegowinisch', 'bosnisch-herzegowinisch'), ('botsuanisch', 'botsuanisch'), ('brasilianisch', 'brasilianisch'), ('bruneiisch', 'bruneiisch'), ('bulgarisch', 'bulgarisch'), ('burkinisch', 'burkinisch'), ('burundisch', 'burundisch'), ('cabo-verdisch', 'cabo-verdisch'), ('chilenisch', 'chilenisch'), ('chinesisch', 'chinesisch'), ('costa-ricanisch', 'costa-ricanisch'), ('ivorisch', 'ivorisch'), ('dänisch', 'dänisch'), ('deutsch', 'deutsch'), ('dominikanisch', 'dominikanisch'), ('dschibutisch', 'dschibutisch'), ('ecuadorianisch', 'ecuadorianisch'), ('salvadorianisch', 'salvadorianisch'), ('eritreisch', 'eritreisch'), ('estnisch', 'estnisch'), ('fidschianisch', 'fidschianisch'), ('finnisch', 'finnisch'), ('französisch', 'französisch'), ('gabunisch', 'gabunisch'), ('gambisch', 'gambisch'), ('georgisch', 'georgisch'), ('ghanaisch', 'ghanaisch'), ('grenadisch', 'grenadisch'), ('griechisch', 'griechisch'), ('guatemaltekisch', 'guatemaltekisch'), ('guineisch', 'guineisch'), ('guinea-bissauisch', 'guinea-bissauisch'), ('guyanisch', 'guyanisch'), ('haitianisch', 'haitianisch'), ('honduranisch', 'honduranisch'), ('indisch', 'indisch'), ('indonesisch', 'indonesisch'), ('irakisch', 'irakisch'), ('iranisch', 'iranisch'), ('irisch', 'irisch'), ('isländisch', 'isländisch'), ('israelisch', 'israelisch'), ('italienisch', 'italienisch'), ('jamaikanisch', 'jamaikanisch'), ('japanisch', 'japanisch'), ('jemenitisch', 'jemenitisch'), ('jordanisch', 'jordanisch'), ('kambodschanisch', 'kambodschanisch'), ('kamerunisch', 'kamerunisch'), ('kanadisch', 'kanadisch'), ('kasachisch', 'kasachisch'), ('katarisch', 'katarisch'), ('kenianisch', 'kenianisch'), ('kirgisisch', 'kirgisisch'), ('kiribatisch', 'kiribatisch'), ('kolumbianisch', 'kolumbianisch'), ('komorisch', 'komorisch'), ('kongolesisch', 'kongolesisch'), ('der Demokratischen Republik Kongo', 'der Demokratischen Republik Kongo'), ('der Demokratischen Volksrepublik Korea', 'der Demokratischen Volksrepublik Korea'), ('der Republik Korea', 'der Republik Korea'), ('kosovarisch', 'kosovarisch'), ('kroatisch', 'kroatisch'), ('kubanisch', 'kubanisch'), ('kuwaitisch', 'kuwaitisch'), ('laotisch', 'laotisch'), ('lesothisch', 'lesothisch'), ('lettisch', 'lettisch'), ('libanesisch', 'libanesisch'), ('liberianisch', 'liberianisch'), ('libysch', 'libysch'), ('liechtensteinisch', 'liechtensteinisch'), ('litauisch', 'litauisch'), ('luxemburgisch', 'luxemburgisch'), ('madagassisch', 'madagassisch'), ('malawisch', 'malawisch'), ('malaysisch', 'malaysisch'), ('maledivisch', 'maledivisch'), ('malisch', 'malisch'), ('maltesisch', 'maltesisch'), ('marokkanisch', 'marokkanisch'), ('marshallisch', 'marshallisch'), ('mauretanisch', 'mauretanisch'), ('mauritisch', 'mauritisch'), ('mazedonisch', 'mazedonisch'), ('mexikanisch', 'mexikanisch'), ('mikronesisch', 'mikronesisch'), ('moldauisch', 'moldauisch'), ('monegassisch', 'monegassisch'), ('mongolisch', 'mongolisch'), ('montenegrinisch', 'montenegrinisch'), ('mosambikanisch', 'mosambikanisch'), ('myanmarisch', 'myanmarisch'), ('namibisch', 'namibisch'), ('nauruisch', 'nauruisch'), ('nepalesisch', 'nepalesisch'), ('neuseeländisch', 'neuseeländisch'), ('nicaraguanisch', 'nicaraguanisch'), ('niederländisch', 'niederländisch'), ('nigrisch', 'nigrisch'), ('nigerianisch', 'nigerianisch'), ('norwegisch', 'norwegisch'), ('omanisch', 'omanisch'), ('österreichisch', 'österreichisch'), ('pakistanisch', 'pakistanisch'), ('palauisch', 'palauisch'), ('panamaisch', 'panamaisch'), ('papua-neuguineisch', 'papua-neuguineisch'), ('paraguayisch', 'paraguayisch'), ('peruanisch', 'peruanisch'), ('philippinisch', 'philippinisch'), ('polnisch', 'polnisch'), ('portugiesisch', 'portugiesisch'), ('ruandisch', 'ruandisch'), ('rumänisch', 'rumänisch'), ('russisch', 'russisch'), ('salomonisch', 'salomonisch'), ('sambisch', 'sambisch'), ('samoanisch', 'samoanisch'), ('san-marinesisch', 'san-marinesisch'), ('são-toméisch', 'são-toméisch'), ('saudi-arabisch', 'saudi-arabisch'), ('schwedisch', 'schwedisch'), ('schweizerisch', 'schweizerisch'), ('senegalesisch', 'senegalesisch'), ('serbisch', 'serbisch'), ('seychellisch', 'seychellisch'), ('sierra-leonisch', 'sierra-leonisch'), ('simbabwisch', 'simbabwisch'), ('singapurisch', 'singapurisch'), ('slowakisch', 'slowakisch'), ('slowenisch', 'slowenisch'), ('somalisch', 'somalisch'), ('spanisch', 'spanisch'), ('sri-lankisch', 'sri-lankisch'), ('von St. Kitts und Nevis', 'von St. Kitts und Nevis'), ('lucianisch', 'lucianisch'), ('vincentisch', 'vincentisch'), ('südafrikanisch', 'südafrikanisch'), ('sudanesisch', 'sudanesisch'), ('südsudanesisch', 'südsudanesisch'), ('surinamisch', 'surinamisch'), ('swasiländisch', 'swasiländisch'), ('syrisch', 'syrisch'), ('tadschikisch', 'tadschikisch'), ('tansanisch', 'tansanisch'), ('thailändisch', 'thailändisch'), ('von Timor-Leste', 'von Timor-Leste'), ('togoisch', 'togoisch'), ('tongaisch', 'tongaisch'), ('von Trinidad und Tobago', 'von Trinidad und Tobago'), ('tschadisch', 'tschadisch'), ('tschechisch', 'tschechisch'), ('tunesisch', 'tunesisch'), ('türkisch', 'türkisch'), ('turkmenisch', 'turkmenisch'), ('tuvaluisch', 'tuvaluisch'), ('ugandisch', 'ugandisch'), ('ukrainisch', 'ukrainisch'), ('ungarisch', 'ungarisch'), ('uruguayisch', 'uruguayisch'), ('usbekisch', 'usbekisch'), ('vanuatuisch', 'vanuatuisch'), ('vatikanisch', 'vatikanisch'), ('venezolanisch', 'venezolanisch'), ('der Vereinigten Arabischen Emirate', 'der Vereinigten Arabischen Emirate'), ('amerikanisch', 'amerikanisch'), ('britisch', 'britisch'), ('vietnamesisch', 'vietnamesisch'), ('weißrussisch', 'weißrussisch'), ('zentralafrikanisch', 'zentralafrikanisch'), ('zyprisch', 'zyprisch')], max_length=255, null=True, verbose_name='Staatsangehörigkeit')),
                ('kommunikationssprache', salesforce.fields.CharField(blank=True, choices=[('deutsch', 'deutsch'), ('englisch', 'englisch')], max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'db_table': 'Account',
                'abstract': False,
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, db_column='Id', primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', salesforce.fields.BooleanField(default=False, verbose_name='Deleted')),
                ('last_name', salesforce.fields.CharField(max_length=80)),
                ('first_name', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('salutation', salesforce.fields.CharField(blank=True, choices=[('Mr.', 'Herr'), ('Ms.', 'Frau'), ('Mrs.', 'Frau'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.')], max_length=40, null=True)),
                ('name', salesforce.fields.CharField(max_length=121, verbose_name='Full Name')),
                ('title', salesforce.fields.CharField(blank=True, max_length=128, null=True)),
                ('email', salesforce.fields.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_phone', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('home_phone', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('other_phone', salesforce.fields.CharField(blank=True, max_length=40, null=True)),
                ('bic', salesforce.fields.CharField(blank=True, db_column='BIC__c', max_length=255, null=True, verbose_name='BIC')),
                ('iban', salesforce.fields.CharField(blank=True, db_column='IBAN__c', max_length=255, null=True, verbose_name='IBAN')),
                ('kontoinhaber', salesforce.fields.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'Contact',
                'abstract': False,
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, db_column='Id', primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', salesforce.fields.BooleanField(default=False, verbose_name='Deleted')),
                ('payment_interval', salesforce.fields.CharField(blank=True, choices=[('Zu Beginn jeden Monats', 'Zu Beginn jeden Monats'), ('Zu Beginn jeden Semesters', 'Zu Beginn jeden Semesters')], max_length=255, null=True, verbose_name='Zahlungsfrequenz')),
            ],
            options={
                'verbose_name': 'Contract',
                'verbose_name_plural': 'Contracts',
                'db_table': 'Contract',
                'abstract': False,
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rabatt',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, db_column='Id', primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', salesforce.fields.BooleanField(default=False, verbose_name='Deleted')),
                ('name', salesforce.fields.CharField(max_length=80, verbose_name='Rabatt')),
                ('discount_type', salesforce.fields.CharField(blank=True, choices=[('Discount Tuition Fee', 'Discount Tuition Fee'), ('Discount Semester Fee', 'Discount Semester Fee')], max_length=255, null=True)),
                ('discount_tuition_fee', salesforce.fields.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Rabatt auf Studiengang')),
                ('discount_semester_fee', salesforce.fields.DecimalField(blank=True, decimal_places=0, max_digits=18, null=True, verbose_name='Rabatt auf Semesterbeitrag')),
                ('applicable_months', salesforce.fields.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='Anzahl anwendbarer Monate')),
                ('utilization', salesforce.fields.DecimalField(blank=True, decimal_places=0, max_digits=18, null=True, verbose_name='Anzahl Anwendungen')),
                ('active', salesforce.fields.BooleanField(default=salesforce.backend.operations.DefaultedOnCreate(), verbose_name='Aktiv')),
            ],
            options={
                'verbose_name': 'Rabatt',
                'verbose_name_plural': 'Rabatte',
                'db_table': 'Rabatt__c',
                'abstract': False,
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecordType',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(auto_created=True, db_column='Id', primary_key=True, serialize=False, verbose_name='ID')),
                ('name', salesforce.fields.CharField(max_length=80)),
                ('developer_name', salesforce.fields.CharField(max_length=80, verbose_name='Record Type Name')),
                ('sobject_type', salesforce.fields.CharField(choices=[('Account', None), ('Announcement', None), ('Asset', None), ('AssetRelationship', None), ('AssistantProgress', None), ('Campaign', None), ('CampaignMember', None), ('Case', None), ('CollaborationGroup', None), ('CollaborationGroupRecord', None), ('ComponentResponseCache', None), ('Contact', None), ('ContentVersion', None), ('Contract', None), ('CustomerBankAccount__c', None), ('DegreeCourse__c', None), ('dlrs__LookupChild__c', None), ('dlrs__LookupChildAReallyReallyReallyBigBigName__c', None), ('dlrs__LookupParent__c', None), ('dlrs__LookupRollupCalculateJob__c', None), ('dlrs__LookupRollupSummary__c', None), ('dlrs__LookupRollupSummaryLog__c', None), ('dlrs__LookupRollupSummaryScheduleItems__c', None), ('DuplicateErrorLog', None), ('DuplicateRecordItem', None), ('DuplicateRecordSet', None), ('Event', None), ('FileSearchActivity', None), ('GoCardlessEvent__c', None), ('Idea', None), ('InboundSocialPost', None), ('Invoice__c', None), ('InvoiceLineItem__c', None), ('Lead', None), ('Macro', None), ('MacroAction', None), ('MacroInstruction', None), ('ManagedContentBlock', None), ('ManagedContentBlockVersion', None), ('Mandate__c', None), ('Opportunity', None), ('Order', None), ('Payment__c', None), ('Pricebook2', None), ('Product2', None), ('ProfileSkill', None), ('ProfileSkillEndorsement', None), ('ProfileSkillUser', None), ('RecordOrigin', None), ('SearchActivity', None), ('SearchPromotionRule', None), ('SetupAssistantAnswer', None), ('SetupAssistantProgress', None), ('SocialPost', None), ('Solution', None), ('SyncTransactionLog', None), ('Task', None), ('UserMetrics', None), ('WorkAccess', None), ('WorkBadge', None), ('WorkBadgeDefinition', None), ('WorkThanks', None)], max_length=40, verbose_name='Sobject Type Name')),
                ('is_active', salesforce.fields.BooleanField(default=False, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Record Type',
                'verbose_name_plural': 'Record Types',
                'db_table': 'RecordType',
                'abstract': False,
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAccount',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('integration.account',),
        ),
        migrations.CreateModel(
            name='UniversityAccount',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('integration.account',),
        ),
        migrations.CreateModel(
            name='UniversityContact',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('integration.contact',),
        ),
    ]
