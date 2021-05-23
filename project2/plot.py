import matplotlib.pyplot as plt
import numpy as np

losses = [0.2523237198591232, 0.2517003074288368, 0.25118258148431777, 0.25075354278087614, 0.25038427114486694, 0.25005258470773695, 0.2497444838285446, 0.24945162385702133, 0.24916651099920273, 0.24888347685337067, 0.24859793186187745, 0.2483057975769043, 0.24801134467124938, 0.24771273136138916, 0.2473994627594948, 0.24706522822380067, 0.24670525938272475, 0.24631590843200685, 0.24589510411024093, 0.2454386368393898, 0.24493677765130997, 0.24438005834817886, 0.24374423623085023, 0.24305064380168914, 0.2422913581132889, 0.2414514809846878, 0.24051590859889985, 0.23947113305330275, 0.2383066773414612, 0.23701805919408797, 0.23558934777975082, 0.2340041145682335, 0.23226663172245027, 0.2303305447101593, 0.22815399765968322, 0.22574519664049147, 0.22310350090265274, 0.22020205706357956, 0.21701882928609847, 0.21352009773254393, 0.20969559252262115, 0.2055331289768219, 0.2010292187333107, 0.19617253839969634, 0.19094836860895156, 0.1853657752275467, 0.17942852079868316, 0.1731581673026085, 0.16654035151004792, 0.15956300795078276, 0.15232792347669602, 0.14502171128988267, 0.1376812383532524, 0.1304257556796074, 0.12327003106474876, 0.11636588796973228, 0.1097885474562645, 0.10357549265027047, 0.09781694263219834, 0.09249856695532799, 0.08762018382549286, 0.08316690996289253, 0.07910251840949059, 0.07539054527878761, 0.07197819836437702, 0.06886245496571064, 0.06600296832621097, 0.06337681487202644, 0.0609555259346962, 0.05872438549995422, 0.05665809251368046, 0.054729167744517325, 0.05294664725661278, 0.051289217174053194, 0.04973609410226345, 0.04828712828457356, 0.04691844098269939, 0.045628726668655875, 0.044421376287937166, 0.04327977001667023, 0.04220593087375164, 0.041189190745353696, 0.04021612610667944, 0.0392931018024683, 0.038418622501194474, 0.03759128954261541, 0.036803100258111954, 0.03605416491627693, 0.035346824675798416, 0.03467855416238308, 0.03404069673269987, 0.03342877011746168, 0.032844404131174086, 0.03228354640305042, 0.03173722494393587, 0.031216256506741046, 0.030719197168946267, 0.030241300724446772, 0.029781049489974974, 0.02933681197464466, 0.028903652727603913, 0.02849057875573635, 0.028088616393506526, 0.027704174630343914, 0.02732930313795805, 0.026972937770187853, 0.02662593834102154, 0.02629157491028309, 0.025966300629079342, 0.025651188939809798, 0.025346267223358154, 0.025052679143846034, 0.02476581446826458, 0.024488723278045653, 0.024223675951361656, 0.023963521420955657, 0.023710177280008793, 0.02346072606742382, 0.023223983682692052, 0.022987362183630466, 0.022758893482387067, 0.022539497725665568, 0.022324448078870775, 0.022110930643975735, 0.021902330033481122, 0.021705098263919354, 0.021512517146766184, 0.021314323879778385, 0.021135186962783336, 0.020948319882154464, 0.020765090361237526, 0.020602346397936344, 0.020426092203706503, 0.02026843708008528, 0.02010564198717475, 0.019943901523947715, 0.0197932786308229, 0.01963937859982252, 0.019470903649926187, 0.01932412637397647, 0.019161897245794535, 0.01900309110060334, 0.018855096958577632, 0.01867885123938322, 0.01853378685191274, 0.018377616815268994, 0.0182380267418921, 0.018099304102361203, 0.017979433108121157, 0.017839175183326006, 0.017705457098782063, 0.017588976211845873, 0.017447738349437712, 0.017340320535004138, 0.017195995803922413, 0.01708794282749295, 0.016956584714353084, 0.016848198417574168, 0.016723482776433228, 0.01663188189268112, 0.016511094663292168, 0.016418674401938914, 0.01631816430017352, 0.01619440345093608, 0.016111246589571238, 0.016002167854458092, 0.015924592968076468, 0.015810184460133315, 0.015729514975100757, 0.01563500240445137, 0.015531424339860678, 0.015439240634441376, 0.015367539320141076, 0.01526688588783145, 0.015162256546318531, 0.01507759103551507, 0.014983076695352792, 0.0149002387188375, 0.014803795237094164, 0.014710770267993212, 0.014635505992919207, 0.014554362557828427, 0.014470400847494602, 0.014410228189080953, 0.014306673593819142, 0.014253222942352295, 0.01416061855852604, 0.01409954223781824, 0.014007225539535284, 0.013938909117132425, 0.013883293326944112, 0.013789619319140911, 0.01374368155375123, 0.013655339647084475, 0.013611929584294557, 0.01351715475320816, 0.013468402996659279, 0.013385935686528683, 0.013314571045339108, 0.013258102722465992, 0.01319171441718936, 0.01312234727665782, 0.01305356528609991, 0.013005103264003993, 0.012938249111175536, 0.012888702377676965, 0.012815328408032655, 0.01276193168014288, 0.012700425367802382, 0.01264042491093278, 0.012579691410064698, 0.012538057658821345, 0.012491594441235066, 0.012415399122983218, 0.01236793203279376, 0.012315483018755912, 0.012264091614633798, 0.012229764834046364, 0.012158837262541055, 0.01210794160142541, 0.012074075918644667, 0.012007994670420885, 0.011960338987410068, 0.011929056700319051, 0.011863786540925503, 0.011835301388055086, 0.011772971134632826, 0.011746740993112325, 0.011667820764705539, 0.011644803406670689, 0.01161251231096685, 0.011550209252163768, 0.011506054596975446, 0.01147006624378264, 0.011422514310106635, 0.011400517914444208, 0.0113482681568712, 0.011295712552964687, 0.011250418657436968, 0.011211464973166585, 0.011177603574469685, 0.011128375586122275, 0.011105434177443385, 0.011044263979420066, 0.011028369702398778, 0.010969143128022552, 0.010957247531041502, 0.010922903846949338, 0.010846324218437075, 0.010825402708724141, 0.01080307704396546, 0.010757818212732672, 0.01072137700393796, 0.010694034676998854, 0.010646324884146453, 0.010632945830002427, 0.01057509114034474, 0.01053584567271173, 0.010528986575081944, 0.010470412950962783, 0.010449509508907795, 0.010385214723646641, 0.01037206407636404, 0.01032905071042478, 0.01030229707248509, 0.010260078124701977, 0.010219900356605648, 0.010201155301183462, 0.010155962686985731, 0.010128199262544513, 0.01011271751485765, 0.010086720762774348, 0.010035134479403495, 0.010016276221722364, 0.009998975647613406, 0.009959906851872802, 0.009930290281772614, 0.009912664210423828, 0.009886372601613402, 0.00985129908658564, 0.009811546420678496, 0.009804441127926111, 0.009776767576113343, 0.009733427967876195, 0.009721515700221062, 0.009690685477107764, 0.009673585277050733, 0.009633622551336884, 0.009609245928004384, 0.009602697333320975, 0.009562672208994627, 0.009534188127145172, 0.009524079179391265, 0.009478679345920681, 0.009465592633932828, 0.009437321778386831, 0.009416210651397704, 0.009394718892872333, 0.009373227367177606, 0.009351080795750023]

x = range(1, len(losses)+1)
plt.plot(x, losses, label='ReLU')
plt.xlabel('epochs')
plt.ylabel('Training Loss')
plt.legend()
#plt.savefig("resnet_loss.png")
plt.show()