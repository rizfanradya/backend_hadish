-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 11, 2024 at 01:05 PM
-- Server version: 8.0.37-0ubuntu0.22.04.3
-- PHP Version: 8.1.2-1ubuntu2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hadish`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('8cc0553b0274');

-- --------------------------------------------------------

--
-- Table structure for table `hadith`
--

CREATE TABLE `hadith` (
  `id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `hadith_arab` text,
  `hadith_melayu` text,
  `explanation` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hadith`
--

INSERT INTO `hadith` (`id`, `created_at`, `updated_at`, `created_by`, `updated_by`, `hadith_arab`, `hadith_melayu`, `explanation`) VALUES
(1, '2024-07-10 10:24:41', NULL, 1, 1, 'كان رسول الله صلى الله عليه وسلم يجهر بسم الله الرحمن الرحيم', '', '[Mustadrak 1: 208] Pernah Rasulullah SAW menyaringkan bacaan Bismillah al-Rahman al-Rahim..\n\nUlasan al-Hakim: Hadis ini sahih sanadnya, tiada kecacatan padanya dan tidak dikeluarkan dalam Sahihain , Ulasan al-Dhahabi (t.th [b], 1:208): Sahih tiada kecacatan padanya! Itulah dakwaan al-Hakim. Namun, ramai ulama menganggap Abdullah ibn \'Amr ibn Hassan pendusta, dan beliau seharusnya mengetahui perkara ini. Ulasan al-Zaila\'i , (1997, 1:345): Hadis ini tidak jelas maknanya dan tidak sahih hukumnya. Ini kerana, matan hadis ini tidak menyatakan sama ada bacaan bismillah tersebut ketika solat ataupun tidak, dan ia tidak sahih kerana terdapat Abdullah ibn \'Amr al-Waqi\'i yang terkenal sebagai pemalsu hadits seperti yang dijelaskan oleh \'Ali ibn al-Madini. \n\nAbdul Rahman ibn Abu Hatim berkata: \"Aku bertanyakan bapaku mengenai (perawi ini) lalu beliau berkata: Tidak dapat diterima, beliau seorang yang berdusta\".\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Ini berdasarkan kewujudan Abdullah ibn \'Amr ibn Hassan al-Waqi\'i pada sanadnya yang dituduh Hadis-hadis Palsu dalam Mustadrak al-Hakim\n\nberdusta oleh \'Ali ibn al-Madini, al-Dar al-Qutni dan al-Dhahabi (t.th. (a), 2:468; Ibn al-Mulaggin 1990, 1:173-177).'),
(2, '2024-07-10 10:24:41', NULL, 1, 1, 'أن رسول الله صلى الله عليه وسلم كان يكبر يوم الفطر من حين يخرج من بيته حتى يأتي المصلي', '', '[Mustadrak 1: 297-298] Rasulullah SAW bertakbir pada hari raya (Aidilfitri) daripada mula keluar rumah sehinggalah baginda sampai ke tempat sembahyang.\n\nUlasan al-Hakim: Hadis ini gharib sanad dan matannya. al- Bukhari dan Muslim juga tidak menerima periwayatan al- Walid ibn Muhammad al-Muwaqqari dan Musa ibn Ata al-Balgawi Ulasan al-Dhahabi (t.th.[b], 1:298): Kedua-duanya (al-Walid dan Musa) adalah matruk.\n\nHukum Hadis:\n\nSelain periwayatan al-Hakim, matan hadis ini turut diriwayatkan oleh ulama lain dengan sanad berbeza dan statusnya adalah sahih menurut ulama (al-Albani 1979, 3:122-123). Walau bagaimanapun, sanad al-Hakim berstatus mawdu\'. Ini berdasarkan kewujudan dua orang perawinya yang dipertikaikan status mereka. al-Walid ibn Muhammad al-Muwaqqari dituduh berdusta dan meriwayatkan hadis-hadis yang tidak berasas, namun kebanyakan ulama menganggapnya lemah sahaja. Sebaliknya, Musa ibn Muhammad ibn \'Ata\' al-Balqawi dihukumkan oleh Abu Hatim, Abu Zur\'ah dan Ibn Hibban sebagai pendusta dan pemalsu hadis. Menurut Mansur ibn Isma\'il ibn Abu Qurrah, Musa pernah memalsukan hadis-hadis yang diriwayatkan oleh Malik dan al- Muwaqqari (al-Asqallani 2002, 8:216-218; 1907, 11:148-150; Ibn al- Mulaggin 1990, 1:240-243).'),
(3, '2024-07-10 10:24:41', NULL, 1, 1, 'عن عروة بن مضرس الطائي رضي الله عنه قال : جنت رسول الله صلى الله عليه وسلم وهو بالموقف فقلت يا رسول الله أتيت من جبل طى أكللت مطيتي واتعبت نفسي والله ما بقي من جبل من تلك الجبال صلاة الغداة يعني إلا وقفت عليه، فقال من أدرك معنا هذه الصلاة وقد أتى عرفة قبل ذلك ليلا أو نهارا فقد تم حجه وقضى تفته', '', '[Mustadrak 1: 463] \'Urwah ibn Mudris al-Ta\'i r.a. berkata: Aku berjumpa Rasulullah SAW ketika baginda berada di tempat rehatnya lalu berkata: Wahai Rasulullah! Aku datang dari arah Bukit Tai\' dan tungganganku telah keletihan serta badanku penat. Demi Allah! Aku tidak tinggalkan satu pun daripada bukit-bukit tersebut melainkan aku berwuquf padanya. Nabi bersabda: Sesiapa yang dapat mengikuti kami pada solat ini (iaitu solat subuh) dan dia telah pergi ke Arafah sebelumnya sama ada malam atau siang, hajinya telah sempurna dan dia telah membersihkan dirinya.\n\nUlasan al-Dhahabi (t.th.[b], 1:463): Yusuf al-Samti tidak thiqah.\n\nHukum Hadis:\n\nSelain periwayatan al-Hakim, matan hadis ini turut diriwayatkan oleh al-Tirmidhi (al-Mubarakfuri 2001, 3:751) dan al-Nasa\'i (t.th., 5:263- 265) dengan sanad berbeza dan hukumnya sahih. Walau bagaimanapun, hadis riwayat al-Hakim ini mawdu\'. Ini berdasarkan kewujudan Yusuf ibn Khalid al-Samti yang dituduh berdusta dan zindik oleh Yahya ibn Ma\'in. Ibn Abu Hatim berkata: \"Aku bertanyakan bapaku mengenai Yusuf al-Samti lalu beliau menjawab: Aku pernah mempertikaikan pandangan Yahya ibn Ma\'in yang mendakwanya sebagai zindik sehinggalah dibawakan kepadaku sebuah buku yang tertulis padanya. hadis-hadis yang dipalsukannya berkaitan akidah dalam pelbagai tajuk termasuklah mengingkari kewujudan timbangan sewaktu kiamat kelak. Terbukti Yahya ibn Ma\'in sebenarnya tidak menuduh secara melulu, bahkan memberikan pandangannya bersandarkan kepada mata hati dan kefahaman yang mendalam\" (al-Razi 1953, 9:221-222). Selain itu, Ibn Hibban (2000, 2:484) dan Abu Ja\'far ibn Nufail turut menyifatkan Yusuf al-Samti sebagai pemalsu hadis dan periwayatannya sama sekali tidak boleh dijadikan pegangan (al-Dhahabi t.th.[a], 4:463-464; Ibn al- Mulaqqin 1990, 1:348-350).'),
(4, '2024-07-10 10:24:41', NULL, 1, 1, 'الله صلى الله عليه وسلم : من استطاع منكم أن يقي دينه\n\nقال رسول\n\nوعرضه بماله فليفعل', '', '[Mustadrak 2: 50] Rasulullah SAW bersabda: Sesiapa dari kalangan kamu yang mampu untuk memelihara diri dan kehormatannya dengan hartanya, maka lakukanlah.\n\nUlasan al-Dhahabi (t.th.[b], 2:50): Abu \'Ismah lemah statusnya.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Pada sanadnya terdapat Abu Ismah Nuh ibn Abu Maryam al-Qurashi yang dilabel sebagai pemalsu hadis dan perawi hadis palsu oleh Ibn al-Mubarak dan Abu Sa\'id al- Naqqash. Abu \'Ali al-Naisaburi dan Ibn \'Uyainah juga menggelarnya pendusta. Menariknya, al-Hakim sendiri mengaku bahawa Nuh pernah memalsukan hadis berkaitan kelebihan al-Quran. Ibn Hibban berkata: \"Beliau membolak-balikkan sanad dan meriwayatkan daripada perawi thiqah hadis yang tidak sabit. Tidak harus menjadikannya hujah sama sekali\". Perawi daripada Nuh dalam hadis ini iaitu Hamid ibn Adam turut dilabelkan sebagai pendusta oleh sejumlah ulama termasuk Ibn \'Adi, al-Jawzajani, Ibn Ma\'in dan al-Sulaimani (al-\'Asqallani 2002, 2:536-537; 1907, 10:486-489). al-Albani (1992-, 2:302) turut berpandangan hadis ini palsu.'),
(5, '2024-07-10 10:24:41', NULL, 1, 1, 'نهى رسول الله صلى الله عليه وسلم أن يفرق بين الأم وولدها، فقيل يا\n\nرسول الله إلى متى ؟ قال : حتى يبلغ الغلام وتحيض الجارية', '', '[Mustadrak 2: 55] Rasulullah SAW melarang sesiapa sahaja memisahkan seorang ibu daripada anaknya. Baginda ditanya: Sehingga bilakah wahai Rasulullah? Baginda bersabda: Sehingga baligh bagi kanak- kanak lelaki dan datang haid bagi kanak-kanak perempuan.\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak\n\ndikeluarkan dalam Sahihain. Ulasan al-Dhahabi (t.th.[b], 2:55): Hadis ini palsu dan Ibn Hassan pendusta.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini berstatus mawdu. Pada sanadnya terdapat Abdullah ibn \'Amr ibn Hassan al-Waqi\'i; seorang pendusta seperti yang telah dibincangkan pada hadis nombor 1 (Ibn al-Mulaqqin 1990, 1:567-568).'),
(6, '2024-07-10 10:24:41', NULL, 1, 1, 'أن رسول الله صلى الله عليه وسلم نهى عن السلف في الحيوان', '', '[Mustadrak 2: 57] Rasulullah SAW melarang menjual haiwan yang masih dalam tanggungan (dan pembeli perlu menunggu sehingga waktu tertentu untuk menerimanya).\n\n“Ulasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain. , Ulasan al-Dhahabi (t.th.[b], 2:57): Hadis ini sahih. Ulasan Ibn Mulaqqin (1990, 1:569): al-Dhahabi bersetuju (dengan al-Hakim) mengenai kesahihan hadis ini sedangkan perawinya yang bernama Ishaq (ibn Ibrahim al-Juni) tidak diketahui statusnya seperti yang dijelaskan oleh Ibn Hazm. Dalam karyanya Mizan (al-I\'tidal), al-Dhahabi menyatakan Ishaq juga menggunakan gelaran al-Tabari dan hadis- hadisnya diingkari ulama. Ketahuilah, sebab hadis ini tidak sahih juga ialah kerana (Abdul Malik) al-Zimari juga telah dihukumkan sebagai lemah oleh ramai ulama.”\n\n\nHukum Hadis:\n\nWalaupun kedua-dua al-Hakim dan al-Dhahabi bersetuju dengan kesahihan hadis ini, namun ia sebenarnya mawdu. Pada sanadnya terdapat Ishaq ibn Ibrahim al-Tabari yang memalsukan hadis. Menurut Ibn Hibban (2000, 1:148-150), hadis-hadisnya sangat diingkari kerana diketahui memalsukan periwayatan daripada perawi thiqah. Oleh itu, tidak dibenarkan menulis hadisnya melainkan sebagai peringatan dan takjub sahaja. Pada masa yang sama, status Abdul Malik al-Zimari adalah lemah sahaja dan beliau tidak dituduh berdusta (al-Dhahabi t.th. [a], 2:657; Ibn al-Mulaqqin 1990, 1:569-571).'),
(7, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم : لخير والتطفكم فانكحوا الأكفاء\n\nوانكحوا إليهم', '', '[Mustadrak 2: 163] Rasulullah SAW bersabda: Hendaklah kamu memilih (yang terbaik) untuk benih (keturunan) kamu. Oleh itu, berkahwinlah dan kahwini mereka yang sekufu dengan kamu. > Ulasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain. Ulasan al-Dhahabi (t.th.[b], 2:163): al-Harith dituduh berdusta dan \'Ikrimah pula lemah statusnya.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Menurut Abu Hatim, al-Harith ibn \'Imran al-Ja\'fari al-Madani statusnya laysa bi qawiyy, tetapi hadis yang diriwayatkannya daripada Hisham daripada \'Aishah (seperti di atas) tidak berasal daripada Rasulullah SAW. Ibn Hibban berkata: al-Harith memalsukan hadis daripada perawi thiqah, antaranya periwayatan daripada Hisham iaitu hadis di atas (al-\'Asqallani 1907, 2:152; al-Dhahabi 1987, 1:214).\nsahih juga ialah kerana (Abdul Malik) al-Zimari juga telah dihukumkan sebagai lemah oleh ramai ulama.\n\nHukum Hadis:\n\nWalaupun kedua-dua al-Hakim dan al-Dhahabi bersetuju dengan kesahihan hadis ini, namun ia sebenarnya mawdu. Pada sanadnya terdapat Ishaq ibn Ibrahim al-Tabari yang memalsukan hadis. Menurut Ibn Hibban (2000, 1:148-150), hadis-hadisnya sangat diingkari kerana diketahui memalsukan periwayatan daripada perawi thiqah. Oleh itu, tidak dibenarkan menulis hadisnya melainkan sebagai peringatan dan takjub sahaja. Pada masa yang sama, status Abdul Malik al-Zimari adalah lemah sahaja dan beliau tidak dituduh berdusta (al-Dhahabi t.th. [a], 2:657; Ibn al-Mulaqqin 1990, 1:569-571).'),
(8, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم: تخيروا النطقكم فانكحوا الأكفاء وانكحوا إليهم', '', '[Mustadrak 2: 163] Rasulullah SAW bersabda: Hendaklah kamu memilih (yang terbaik) untuk benih (keturunan) kamu. Oleh itu, berkahwinlah dan kahwini mereka yang sekufu dengan kamu.\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain.\n\nUlasan al-Dhahabi (t.th.[b], 2:163): al-Harith dituduh berdusta dan \'Ikrimah pula lemah statusnya.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Menurut Abu Hatim, al-Harith ibn \'Imran al-Ja\'fari al-Madani statusnya laysa bi qawiyy, tetapi hadis yang diriwayatkannya daripada Hisham daripada \'Aishah (seperti di atas) tidak berasal daripada Rasulullah SAW. Ibn Hibban berkata: al-Harith memalsukan hadis daripada perawi thiqah, antaranya periwayatan daripada Hisham iaitu hadis di atas (al-\'Asqallani 1907. 2:152; al-Dhahabi 1987, 1:214)'),
(9, '2024-07-10 10:24:41', NULL, 1, 1, 'اسلم غيلان بن سلمة الثقفي وله ثمان نسوة فأمره رسول الله صلى\n\nالله عليه وسلم أن يتخير منهن أربعا', '', '[Mustadrak 2: 193] Ketika Ghailan ibn Salamah al-Thaqafi memeluk Islam, beliau mempunyai lapan orang isteri. Rasulullah SAW pun menyuruhnya memilih empat orang sahaja daripada mereka.\n\nUlasan al-Dhahabi (t.th.[b], 2:193): Menurut Ibn Sa\'id, Ahmad ibn Muhammad adalah pendusta. \'Umar ibn Yunus pula tidak pernah berjumpa dengan Yahya ibn Kathir, walaupun Yahya mendengar hadis ini daripada Mi\'mar yang juga muridnya.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Pada sanadnya terdapat Ahmad ibn Muhammad ibn \'Umar, Abu Sahl al-Yamami yang dituduh berdusta oleh Abu Hatim dan Ibn Sa\'id. Menurut Ibn \'Adi, beliau meriwayatkan hadis yang diingkari dan pelik-pelik daripada perawi thiqah (al-Asqallani 2002, 1:629-630; al-Dhahabi t.th.[a], 1:142-143; Ibn al-Mulaqqin 1990, 2:659-661).'),
(10, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم: أهل الجور وأعوانهم في النار', '', '[Mustadrak 4: 89] Rasulullah SAW bersabda: Orang yang melakukan kezaliman dan pembantu-pembantu mereka akan dimasukkan ke dalam neraka kelak.\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain. Ulasan al-Dhahabi (t.th.[b], 4:89): Hadis ini munkar. Hadis-hadis Palsu dalam Mustadrak al-Hakim\n\nHukum Hadis: Terdapat dua perawi hadis ini yang dipertikaikan iaitu Marwan ibn Abdullah dan bapanya yang berstatus majhul. Pada masa yang sama, timbul beberapa persoalan mengenai integriti dan kesahihan maklumat perawi-perawi sanad ini. Pertamanya, Marwan ibn Abdullah direkodkan oleh Ibn Hajar al-\'Asqallani (2002, 6:293, 8:30) sebagai anak kepada Safwan ibn Huzaifah dan bukannya pembantu seperti yang tertera dalam Mustadrak. Keduanya, al-\'Uqaili turut meriwayatkan hadis ini menerusi sanad yang sama namun dengan perbezaan nama, iaitu \"Anbasah ibn Abdul Rahman meriwayatkannya daripada Marwan dan bukannya \"Uyainah seperti dalam riwayat al-Hakim. Ini bermakna, terdapat kesalahan dan pengubahan nama pada sanad hadis ini yang dilakukan oleh pihak tertentu sama ada akibat kelalaian mahupun disengajakan. Ini kerana, walaupun \'Uyainah hanya berstatus da\'if (sekiranya benar ia meriwayatkan hadis ini), namun Anbasah dilabel oleh Abu Hatim sebagai pemalsu hadis (al-Dhahabi 1987, 2:79). Justeru, terdapat perselisihan pandangan dalam kalangan ulama mengenal status hadis ini. Sesetengah berpendapat ia da\'if, namun sesetengah yang lain pula menghukumkan sanad hadis ini mawdu\' (Ibn al-Mulaqqin 1990, 5:2485-6).'),
(11, '2024-07-10 10:24:41', NULL, 1, 1, 'كان النبي صلى الله عليه وسلم يسمى التمر واللين الأطيبان ', '', '[Mustadrak 4: 106] Rasulullah SAW pernah menamakan buah kurma dan susu sebagai \"dua perkara yang baik\".\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain. Ulasan al-Dhahabi (t.th.[b], 4:106): Talhah perawi lemah.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Pada sanadnya terdapat Talhah ibn Zaid al-Raqqi atau al-Qurashi al-Shami yang dilabel sebagai pemalsu hadis oleh Ahmad ibn Hanbal, \'Ali ibn al-Madini dan Abu Dawud. Ibn. Hibban pula menyifatkannya sebagai seorang yang hadisnya sangat diingkari dan tidak boleh dijadikan hujah dalam agama (al-Asqallani 1907, 5:15-16; al-Dhahabi t.th.[a], 2:338-339; Ibn al-Mulaqqin 1990, 5:2549-2550).'),
(12, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم : إن الشيطان حساس الحاس فاحذروه على أنفسكم من بات وفي يده ربح فأصابه شي فلا يلومن\n\nإلا نفسه', '', '[Mustadrak 4: 119] Rasulullah SAW bersabda: Syaitan amat sensitif dengan sebarang bentuk deria dan hendaklah kamu berwaspada daripadanya. Sesiapa yang bermalam dan di tangannya terdapat bau (makanan) dan terkena padanya sesuatu perkara (yang buruk), maka ia tidak boleh menyalahkan sesiapa melainkan dirinya sendiri.\n\nUlasan al-Hakim: Hadis ini sahih berdasarkan syarat al- Bukhari dan Muslim.\n\nUlasan al-Dhahabi (t.th.[b], 4:119): Hadis ini palsu kerana Ya\'qub dituduh berdusta oleh Ahmad (ibn Hanbal) dan ramai lagi.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Pada sanadnya terdapat Ya\'qub ibn al-Walid al-Madani atau al-Azdi yang dilabel sebagai pemalsu hadis oleh Ahmad ibn Hanbal, Abu Hatim (al-Razi 1953, 9:216-217). Ibn Hibban dan Yahya ibn Ma\'in (al-\'Asqallani 1907, 11:397-398; al- Dhahabi 1987, 2:433; Ibn al-Mulaqqin 1990, 5:2579-81).'),
(13, '2024-07-10 10:24:41', NULL, 1, 1, 'عن أبي جحيفة قال: أكلت ثريدة من خبز بر ولحم سمين ثم أتيت النبي صلى الله عليه وسلم فجعلت انجشا فقال: ما هذا كف من جشائك فإن أكثر الناس في الدنيا شبعا أكثرهم في الآخرة جوعا', '', '[Mustadrak 4: 121] Abu Juhaifah berkata: Aku memakan sejenis makanan yang diperbuat daripada roti gandum dan daging berlemak lalu berjumpa Rasulullah SAW dan bersendawa (kekenyangan). Baginda bersabda: Apa ini! Hentikan sendawa kamu, Sesungguhnya ramai daripada orang yang kenyang di dunia akan berlapar di akhirat kelak.  \n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain.\n\nUlasan al-Dhahabi (t.th.[b], 4:121): Fahd seorang pendusta seperti yang dinyatakan oleh (\'Ali ibn) al-Madini, manakala \'Umar ibn Musa pula tidak dapat diterima.'),
(14, '2024-07-10 10:24:41', NULL, 1, 1, ' قال أبو جحيفة: أكلت لحما كثيرا وتريدا\n\n\n ثم جئت فقعدت حيال\n\nالنبي صلى الله عليه وسلم فجعلت الحشا فقال: أقصر من حشائك\n\nفإن أكثر الناس شبعا في الدنيا أكثرهم جوعا في الآخرة', '', '[Mustadrak 4: 311] Abu Juhaifah berkata: Aku pernah makan daging dan sejenis juadah dalam jumlah yang banyak dan kemudiannya berjumpa Rasulullah SAW dan duduk di kalangan baginda lalu bersendawa. Baginda bersabda: Kurangkan bersendawa. Sesungguhnya kebanyakan manusia yang kenyang di dunia akan kelaparan di akhirat kelak.\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain.\n\nUlasan al-Dhahabi (t.th.[b], 4:311): Fahd dituduh berdusta oleh Ibn al-Madini.\n\nHukum Hadis:\n\nDalam Mustadrak, hadis ini disebutkan sebanyak dua kali pada tempat yang berbeza iaitu dalam Bab Makanan dan Bab Melembutkan Hati. Pada hadis pertama, terdapat dua orang perawi yang dipertikaikan status mereka oleh al-Dhahabi. Fahd atau nama sebenarnya Zaid ibn \'Awf dilabel sebagai pendusta dan pemalsu hadis oleh \'Ali ibn al- Madini. Abu Zur\'ah pula menuduhnya mencuri hadis periwayatan orang lain. Demikian juga, \'Umar ibn Musa ibn Wajih al-Wajihi dituduh memalsukan hadis oleh Ibn \'Adi, Abu Hatim dan Yahya ibn Ma\'in Justeru, sanad hadis ini berstatus mawdu. Disebabkan Fahd atau Zaid ibn \'Awf turut terdapat pada sanad hadis kedua, ia juga berstatus mawdu (al-\'Asqallani 2002, 3:559-60, 6:148-151; al-Dhahabi 1987, 2:110). Walau bagaimanapun, matan hadis ini turut diriwayatkan dengan sanad berbeza dan ada di antaranya yang mencapai taraf hasan seperti yang disimpulkan oleh al-Albani (1988, 1:259; Ibn al-Mulaqqin 1990, 5:2605-10, 6:2975).'),
(15, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم: اعتموا تزدادوا حلما', '', '[Mustadrak 4: 193] Rasulullah SAW bersabda: Pakailah serban nescaya bertambah sifat lemah-lembut kamu.\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain.\n\nUlasan al-Dhahabi (t.th.[b], 4:193): Ubaidullah ditinggalkan periwayatannya oleh Ahmad.\n\nHukum Hadis:\n\nPada sanad hadis ini terdapat perawi bernama Ubaidullah ibn Abu Humaid Abu al-Khattab al-Basri. Menurut al-Bukhari, hadis beliau diingkari dan pernah meriwayatkan daripada Abu al-Mulaih perkara yang pelik-pelik. Ibn Hibban pula menyifatkannya sebagai seorang yang suka menterbalikkan sanad dan seharusnya ditolak (al-\'Asqallani 1907, 7:9-10). Justeru, kebanyakan ulama termasuk al-Albani (1992-, 6:341-345; Ibn al-Mulaqqin 1990, 6:2836-38) menyifatkan hadis ini terlalu lemah. Sebahagian ulama pula menghukumkannya palsu (al- Shawkani 1995, 187).'),
(16, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم: من مثل بعيده فهو حر وهو مولى', '', '[Mustadrak 4: 368] Rasulullah SAW bersabda: Sesiapa yang menyeksa hambanya, ia akan menjadi bebas dan menjadi hamba kepada Allah dan rasul- Nya. Hukum Hadis:\n\nstatusnya sebagai perawi hadis-hadis palsu (al-\'Asqallani 1907, 3:28-29: Ibn al-Mulaqqin 1990, 7:3154). Walau bagaimanapun, matan hadis ini turut diriwayatkan oleh ulama lain dengan sanad berbeza dan ada diantaranya yang mencapai status sahih (al-Haithami 1991, 4:436-437).\n\nUlasan al-Dhahabi (t.th.[b], 4:368): Hamzah ialah al-Nasibi Menurut Ibn \'Adi, beliau pemalsu hadis, Sanad hadis ini mawdu. Padanya terdapat Hamzah Ibn Abu Hamzah al-Jazari al-Nasibi yang dilabel sebagai pemalsu hadis oleh Ibn \'Adi. Ulama lain seperti Ibn Hibban dan al-Hakim sendiri mengakui'),
(17, '2024-07-10 10:24:41', NULL, 1, 1, 'عن عمرو بن العاص رضي الله عنه أنه زار عمة له قدمت له يطعام فابطات الجارية فقالت : ألا تستعجلي يا زانية فقال عمرو: سبحان الله لقد قلت أمرا عظيما هل اطلعت عنها على زني ؟ قالت لا والله فقال عمرو رضي الله عنه : إني سمعت رسول الله صلى الله عليه وسلم يقول : أيما عبد أو أمرأة قال أو قالت لوليدتها يا زانية ولم تطلع منها على زناء جلدتها وليدتها يوم القيامة لأنه لا حد لهن في الدنيا', '', '[Mustadrak 4: 370] \"Amr ibn al-As r.a. menceritakan beliau pernah menziarahi makciknya dan dijemput menikmati hidangan. Apabila anak perempuannya lambat (menghidangkan makanan), makciknya mengherdiknya: \"Cepatlah sedikit wahai penzina! \"Mendengarkan ini Amr berkata: \"Maha suci Allah! Sesungguhnya engkau mendakwa suatu perkara yang besar. Apakah engkau benar-benar tahu anak mu telah berzina?\" Makciknya menjawab: \"Tidak, demi Allah\". \"Amr ra, berkata: \"Aku mendengar Rasulullah SAW bersabda: Mana-mana lelaki atau perempuan yang memanggil anaknya \"Wahai penzina\" sedangkan anaknya tidak melakukannya, ia akan disebat oleh anaknya di akhirat kelak. Ini kerana tiada hukuman bagi pertuduhan ibu bapa (terhadap anaknya) di dunia ini.\" Ulasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain. Ulasan al-Dhahabi (t.th.[b], 4:370): Ulama telah sepakat meninggalkan periwayatan Abdul Malik ibn Harun sehinggakan ada yang menuduhnya sebagai Dajal.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu. Pada sanadnya terdapat Abdul Malik ibn Harun ibn \'Antarah yang dituduh berdusta oleh al-Jawzajani, Yahya ibn Ma\'in, Ibn Hibban dan sebagainya. al-Sa\'di berkata: \"Abdul Malik ibn Harun Dajal dan pendusta\". Menariknya, al-Hakim juga pernah melabel Abdul Malik sebagai perawi hadis palsu, namun hadisnya masih juga dimuatkan dalam Mustadrak dan dihukumkan sahih (al-Asqallani 2002, 5:276-278; al-Dhahabi 1987, 1:579). Dari aspek kandungan, terdapat hadis yang diriwayatkan oleh Abu Hurairah dengan lafaz yang berbeza namun hampir maknanya dengan hadis ini dan ia dihukumkan sahih oleh ulama (al-Albani 1988, 2:1103; Ibn al- Mulaggin 1990, 7:3158-9).'),
(18, '2024-07-10 10:24:41', NULL, 1, 1, 'الله عنه سأل رسول الله صلى الله عليه وسلم وما بينه عفان رضي ! بن أن عثمان عن بسم الله الرحمن الرحيم فقال: هو اسم من أسماء الله و وبين اسم الله الأكبر إلا كما بين سواد العين وبياضها من القرب ', '', '[Mustadrak 1: 552] Uthman ibn \'Affan r.a. bertanyakan Rasulullah SAW mengenai bismillah lalu baginda bersabda: la merupakan salah satu nama Allah. Kedudukannya dengan nama Allah yang Maha Besar adalah seumpama kedudukan antara mata hitam dan mata putih\n\n(iaitu amat dekat).\n\nUlasan al-Hakim: Hadis ini sahih sanadnya dan tidak dikeluarkan dalam Sahihain. Ulasan al-Dhahabi (t.th.[b], 1:552): Hadis ini sahih sanadnya.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim ini mawdu\'. Walaupun al-Dhahabi mengulasnya sebagai sahih sanad, namun dalam karyanya yang lain (t.th.[a], 2:182), beliau telah menyatakan dengan jelas perawi sanad ini iaitu Sallam ibn Wahb al-Janadi telah meriwayatkan daripada Tawus (juga perawi sanad ini) sebuah hadis yang bercanggah lagi dusta mengenai bismillah, iaitu matan yang serupa dengan hadis ini. Ibn Hajar (2002, 4:103-104) turut mengakui hukum yang diberikan al-Dhahabi.'),
(19, '2024-07-10 10:24:41', NULL, 1, 1, 'قال رسول الله صلى الله عليه وسلم: من قرأ عشر آيات في ليلة لم 18. (Muststrok 1: 555-556) الغافلين ومن قرأ مالة آية كتب من القانتين يكتب من ', '', '[Muststrok 1: 555-556] Rasulullah SAW bersabda: Sesiapa yang membaca 10 ayat (alQuran) pada waktu malam, ia tidak akan ditulis sebagai orang yang lalai. Sesiapa yang membaca 100 ayat pula akan ditulis sebagai orang yang taat. Ulasan al-Dhahabi (t.th.[b], 1:556): Sanad ini lemah. Ulasan al-Albani (1995, 2.245); Ternyata Abdullah ialah anak kepada Sam\'an al-Makhzumi al-Madani dan dituduh berdusta.\n\nHukum Hadis:\n\nHadis riwayat al-Hakim menerusi sanad ini adalah mawdu. Pada sanadnya terdapat Abdullah ibn Ziad ibn Sulaiman ibn Sam\'an al- Makhaumi yang dilabel sebagai pendusta dan pemalsu hadis oleh Malik ibn Anas, Hisham ibn \'Urwah, Yahya ibn Ma\'in, Ahmad ibn Salih, Abu Dawud, al-Jawzajani, dan sebagainya. Walau bagaimanapun, matan hadis ini turut diriwayatkan dengan sanad berbeza dan hukumnya sahih seperti periwayatan Ibn Nasr dan Ibn Khuzaimah menerusi Abu Hurairah dan sebagainya (al-\'Asqallani 1907, 5:219-221; al-Albani 1995, 2:244-245; Ibn al-Mulaqqin 1990, 1:472-474).'),
(20, '2024-07-10 10:24:41', NULL, 1, 1, 'كان رسول الله صلى الله عليه وسلم يقرأ إنه عمل غير صالح ', '', '[Mustadrak 2: 2411] Rasulullah SAW pernah membaca (ayat yang bermaksud) \"Sesungguhnya bawaannya bukanlah amal yang salih\" (Hud: 46). Ulasan al-Dhahabi (t.th.[b], 2:241): Sanad ini muzlim. Terdapat beberapa kecelaruan pada sanad hadis ini. Dari satu aspek, beberapa perawinya seperti Abu Zawqah dan Jahadah (bapa Muhammad) tidak dikenali status mereka. Dari aspek yang lain pula, terdapat perawi bernama Muhammad ibn \'Uthman ibn Abu Shaibah yang hebat dipertikaikan ulama dan sebahagian daripada mereka seperti Ibn Khirash, Abdullah ibn Usamah al-Kalbi, Ibrahim ibn Ishaq al-Sawwaf, Dawud ibn Yahya dan Ja\'far ibn Muhammad al-Tayalisi menggelarnya pendusta (al-Asqallani 2002, 7:340342; al-Razi 1953, 1:546). Justeru, sesetengah pengkaji berpandangan hadis riwayat al- Hakim ini palsu berdasarkan situasi sanadnya yang bercelaru dan diselubungi kesamaran (Ibn al-Mulaqqin 1990, 2:710-712),');

-- --------------------------------------------------------

--
-- Table structure for table `hadith_assesment`
--

CREATE TABLE `hadith_assesment` (
  `id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `hadith_id` int DEFAULT NULL,
  `evaluation_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hadith_assesment`
--

INSERT INTO `hadith_assesment` (`id`, `created_at`, `updated_at`, `created_by`, `updated_by`, `user_id`, `hadith_id`, `evaluation_id`) VALUES
(1, '2024-07-10 15:08:37', '2024-07-11 10:46:21', 1, 1, 1, 1, 3),
(2, '2024-07-11 01:04:12', NULL, 3, NULL, 3, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int NOT NULL,
  `role` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `updated_by` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `role`, `created_at`, `updated_at`, `created_by`, `updated_by`) VALUES
(1, 'SUPER ADMIN', '2024-07-10 04:31:06', NULL, 0, NULL),
(2, 'ADMIN', '2024-07-10 04:31:10', NULL, 0, NULL),
(3, 'EXPERT', '2024-07-10 04:31:15', NULL, 0, NULL),
(4, 'USER', '2024-07-10 04:31:20', NULL, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `type_hadith`
--

CREATE TABLE `type_hadith` (
  `id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `type_hadith`
--

INSERT INTO `type_hadith` (`id`, `created_at`, `updated_at`, `created_by`, `updated_by`, `type`) VALUES
(1, '2024-07-10 10:57:25', NULL, 1, NULL, 'Hadish Mutawatir'),
(2, '2024-07-10 10:57:45', NULL, 1, NULL, 'Hadish Sahih'),
(3, '2024-07-10 10:58:00', NULL, 1, NULL, 'Hadish Hasan'),
(4, '2024-07-10 10:58:13', NULL, 1, NULL, 'Hadish Dha\'if'),
(5, '2024-07-10 10:58:22', NULL, 1, NULL, 'Hadish Maudhuk'),
(6, '2024-07-10 10:58:30', NULL, 1, NULL, 'Hadish Ahad');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(300) NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `role` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `created_at`, `updated_at`, `created_by`, `updated_by`, `username`, `first_name`, `last_name`, `email`, `password`, `status`, `role`) VALUES
(1, '2024-07-10 04:33:12', NULL, 0, NULL, 'superadmin', 'super', 'admin', 'superadmin@gmail.com', '54ae51ae4f31937454db3afdb359823d', 1, 1),
(2, '2024-07-10 04:33:55', NULL, 0, NULL, 'admin', 'admin', '01', 'admin@gmail.com', '4c79273eed3d095e55d1224f6524ae92', 1, 2),
(3, '2024-07-10 04:34:21', NULL, 0, NULL, 'expert', 'expert', '01', 'expert@gmail.com', '8658cf20990a52150ad553d042275012', 1, 3),
(4, '2024-07-10 04:34:44', NULL, 0, NULL, 'user', 'user', '01', 'user@gmail.com', '0f13dcb6729761548649efb47bb2908d', 1, 4),
(5, '2024-07-11 13:00:09', '2024-07-11 13:01:27', 0, 2, 'expert2', 'expert', '02', 'expert2@gmail.com', '8658cf20990a52150ad553d042275012', 1, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `hadith`
--
ALTER TABLE `hadith`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_hadith_id` (`id`);

--
-- Indexes for table `hadith_assesment`
--
ALTER TABLE `hadith_assesment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `evaluation_id` (`evaluation_id`),
  ADD KEY `hadith_id` (`hadith_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `ix_hadith_assesment_id` (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `role` (`role`),
  ADD KEY `ix_role_id` (`id`);

--
-- Indexes for table `type_hadith`
--
ALTER TABLE `type_hadith`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `type` (`type`),
  ADD KEY `ix_type_hadith_id` (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `ix_user_id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hadith`
--
ALTER TABLE `hadith`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `hadith_assesment`
--
ALTER TABLE `hadith_assesment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `type_hadith`
--
ALTER TABLE `type_hadith`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hadith_assesment`
--
ALTER TABLE `hadith_assesment`
  ADD CONSTRAINT `hadith_assesment_ibfk_1` FOREIGN KEY (`evaluation_id`) REFERENCES `type_hadith` (`id`),
  ADD CONSTRAINT `hadith_assesment_ibfk_2` FOREIGN KEY (`hadith_id`) REFERENCES `hadith` (`id`),
  ADD CONSTRAINT `hadith_assesment_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
