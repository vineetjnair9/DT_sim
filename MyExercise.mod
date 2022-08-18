(EGEMOL6:
	VSD::ModelNode(
		(extensions = [
			VSPluginRBDynamX::SimStateExtension(
			)
			VSPluginRBDynamX::ExtensionDynamXScene(
				(gravity = "(0,0,-9.8066499999999994)")
			)
		])
		(name = "Model")
		(flags = "Show | Select")
		(childNodes = [
			VSD3D::Node(
				(name = "Robot")
				(flags = "Show | Select")
				(childNodes = [
					SDULibServiceBlocksI40::Agent::Kin(
						(myModelInstanceId = "1775")
						(name = "RobotAgent")
						(flags = "Show | Select")
						(root = instance(1789,52))
						(tcp = instance(1789,1754))
					)
					VSD::ModelNode(
						(myModelInstanceId = "1789")
						(name = "UR5e A")
						(flags = "Show | Select")
						(url = "./Comp/UR5eA.MOD")
					)
				])
			)
			SDUPluginServiceBlocksDemo::PythonPath(
				(myModelInstanceId = "1793")
				(extensions = [
					VSPluginVSDIOEditor::PosExtension(
						(x = "-715.60446914587669")
						(y = "-44.969623540885067")
					)
					VSDIO::ExtensionIOBoard(
						(inputs = [
							VSDIO::InputBool(
								(myModelInstanceId = "1783")
								(name = "Enabled")
							)
						])
						(outputs = [
							VSDIO::OutputBool(
								(myModelInstanceId = "1784")
								(name = "Finished successfully")
							)
							VSDIO::OutputBool(
								(myModelInstanceId = "1785")
								(name = "Finished with error")
							)
							VSDIO::OutputInteger(
								(myModelInstanceId = "1786")
								(name = "Error code")
							)
							VSDIO::OutputQString(
								(myModelInstanceId = "1787")
								(name = "Error message")
							)
							VSDIO::OutputVSDRef(
								(myModelInstanceId = "1788")
								(name = "Pose List")
							)
							VSDIO::OutputVSDRef(
								(myModelInstanceId = "1794")
								(name = "pathPoseList")
							)
						])
					)
					VSLibIOTools::PropertyToOutputExtension(
						(name = "PropertyToOutput_pathPoseList")
						(targetPropertyName = "pathPoseList")
						(outputForPropValue = instance(1794))
					)
				])
				(flags = "Show | Select")
				(childNodes = [
					VSLibPoseList::PoseList(
						(myModelInstanceId = "1774")
						(name = "Robot Path")
						(flags = "Select")
						(posesRadius = "0.050000000000000003")
						(posesColor = "(84,171,255)")
						(isAutoCreated = "0")
					)
					VSLibPoseList::Pose(
						(myModelInstanceId = "1790")
						(name = "StartPose")
						(flags = "Show | Select")
						(relFrameTransform = 
							VSD3D::FrameTransform(
								(relFrame = "(-0.9996863996126919,-0.0012218331400557503,0.025012188092836889,-0.46350337391840918,-0.00059857063813412159,0.99968950144099511,0.024910688907490947,-0.43565758311153696,-0.025034858549725345,0.024887905344413583,-0.99937672977959757,0.20202111978860826,0,0,0,1)")
							)
						)
						(definition = 
							VSLibPoseList::JointPoseExtension(
								(jointValues = ["-2.177051105058704" "-2.0800777200770728" "-1.6835917027065748" "-0.98345032841608448" "1.5771571269607811" "-0.60727573324114725"])
							)
						)
						(associatedKinematic = instance(1789,52))
					)
					VSLibPoseList::Pose(
						(myModelInstanceId = "1791")
						(name = "EndPose")
						(flags = "Show | Select")
						(relFrameTransform = 
							VSD3D::FrameTransform(
								(relFrame = "(-0.9996863996126919,-0.0012218331400556948,0.025012188092836535,0.14183787860504088,-0.00059857063813412159,0.999689501440995,0.024910688907491148,-0.43565758311153691,-0.025034858549724936,0.024887905344413801,-0.99937672977959757,0.20202111978860837,0,0,0,1)")
							)
						)
						(definition = 
							VSLibPoseList::JointPoseExtension(
								(jointValues = ["-0.9687151189777885" "-1.7263983666942586" "-2.2109010868260119" "-0.78145789433386748" "1.6055257113757224" "0.60106012583145474"])
							)
						)
						(associatedKinematic = instance(1789,52))
					)
				])
				(inputDataList = [
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1783))
						(metaPropertyName = "enabled")
					)
				])
				(outputDataList = [
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1784))
						(metaPropertyName = "success")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1785))
						(metaPropertyName = "error")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1786))
						(metaPropertyName = "errorCode")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1787))
						(metaPropertyName = "errorMessage")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1788))
						(metaPropertyName = "pathPoseList")
					)
				])
				(startPose = instance(1790))
				(endPose = instance(1795))
				(pathPoseList = instance(1774))
				(collisonRoot = instance(1789,52))
			)
			VSD3D::CameraNode(
				(myModelInstanceId = "1")
				(flags = "Show | Select")
				(relFrameTransform = 
					VSD3D::FrameTransform(
						(relFrame = "(0.99132327263307085,0.13137002165682043,0.0044818016404938035,-0.39189584147295903,-0.1240925676536319,0.92407416869521075,0.36150790503581548,-2.9597868133334053,0.043349784188470714,-0.35892735777611312,0.93235827236672875,1.3988396315135101,0,0,0,1)")
					)
				)
				(viewPointFixed = "0")
				(refPointFixed = "0")
				(cameraFixed = "0")
				(viewDirectionFixed = "0")
				(stereoEyeDistance = "0.080000000000000002")
				(parallaxAngle = "0")
				(isPerspective = "1")
				(near = "0.01")
				(far = "10000")
				(fovx = "1.0471975511965976")
				(fovy = "0")
				(fovxChunkCount = "1")
				(orthoFOV = "400")
				(distanceToRefPoint = "3.4888207638131696")
				(maxZoomOrtho = "1e+308")
				(minZoomOrtho = "0.001")
				(maxRefDist = "1e+308")
				(minRefDist = "0")
			)
			SDULibServiceBlocksI40::Service::Robot::Move::Ptp(
				(extensions = [
					VSDIO::ExtensionIOBoard(
						(inputs = [
							VSDIO::InputBool(
								(myModelInstanceId = "1765")
								(name = "Enabled")
							)
							VSDIO::InputBool(
								(myModelInstanceId = "1766")
								(name = "Run in simulation")
								(localValue = "1")
							)
							VSDIO::InputVSDRef(
								(myModelInstanceId = "1767")
								(name = "Pose List")
							)
						])
						(outputs = [
							VSDIO::OutputBool(
								(myModelInstanceId = "1768")
								(name = "Finished successfully")
							)
							VSDIO::OutputBool(
								(myModelInstanceId = "1769")
								(name = "Finished with error")
							)
							VSDIO::OutputInteger(
								(myModelInstanceId = "1770")
								(name = "Error code")
							)
							VSDIO::OutputQString(
								(myModelInstanceId = "1771")
								(name = "Error message")
							)
						])
					)
					VSPluginVSDIOEditor::PosExtension(
						(x = "-384.01673953170257")
						(y = "-47.023376446275506")
					)
				])
				(flags = "Show | Select")
				(inputDataList = [
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1765))
						(metaPropertyName = "enabled")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1766))
						(metaPropertyName = "runSimulated")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1767))
						(metaPropertyName = "poseList")
					)
				])
				(outputDataList = [
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1768))
						(metaPropertyName = "success")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1769))
						(metaPropertyName = "error")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1770))
						(metaPropertyName = "errorCode")
					)
					SDULibServiceBlocks::IOData(
						(ioElement = instance(1771))
						(metaPropertyName = "errorMessage")
					)
				])
				(runSimulated = "1")
				(executionEngineSimulation = 
					SDULibServiceBlocksI40::ExecutionEngine::Sim::MovePtp::Kinematic(
					)
				)
				(agent = instance(1775))
				(poseList = instance(1774))
				(speed = "1")
				(jointAcc = "0.5")
			)
			VSD::Node(
				(name = "Connections")
				(flags = "Select")
				(childNodes = [
					VSDIO::ConnectionNode(
						(name = "Finished successfully -> Enabled")
						(flags = "Show | Select")
						(output = instance(1784))
						(input = instance(1765))
					)
					VSDIO::ConnectionNode(
						(name = "pathPoseList -> Pose List")
						(flags = "Show | Select")
						(output = instance(1794))
						(input = instance(1767))
					)
				])
			)
			VSD::Node(
				(extensions = [
					VSPluginVSDIOEditor::PosExtension(
						(x = "-550.51130487885143")
						(y = "-259.30186411264481")
					)
				])
				(name = "Macro")
				(flags = "Show | Select")
			)
			VSD3D::Node(
				(name = "Table")
				(flags = "Show | Select")
				(childNodes = [
					VSD::ModelNode(
						(myModelInstanceId = "1792")
						(name = "Table")
						(flags = "Show | Select")
						(url = "./Comp/Table_Difficult.MOD")
					)
				])
				(relFrameTransform = 
					VSD3D::FrameTransform(
					)
				)
			)
			VSD::Node(
				(name = "Collision")
				(flags = "Show | Select")
				(childNodes = [
					SDUPluginClearance::ConnectionNodeClearance(
						(name = "Robot <-> TableEasy")
						(flags = "Show | Select")
						(firstGroupNode = instance(1789,1938))
						(secondGroupNode = instance(1792,6))
						(active = "1")
					)
					SDUPluginClearance::ConnectionNodeClearance(
						(name = "Robot <-> TableMedium")
						(flags = "Show | Select")
						(firstGroupNode = instance(1789,1938))
						(secondGroupNode = instance(1792,7))
						(active = "1")
					)
					SDUPluginClearance::ConnectionNodeClearance(
						(name = "Robot <-> TableDifficult")
						(flags = "Show | Select")
						(firstGroupNode = instance(1789,1938))
						(secondGroupNode = instance(1792,8))
						(active = "1")
					)
					SDUPluginClearance::ConnectionNodeClearance(
						(name = "Gripper <-> TableEasy")
						(flags = "Show | Select")
						(firstGroupNode = instance(1789,1913,73))
						(secondGroupNode = instance(1792,6))
						(active = "1")
					)
					SDUPluginClearance::ConnectionNodeClearance(
						(name = "Gripper <-> TableMedium")
						(flags = "Show | Select")
						(firstGroupNode = instance(1789,1913,73))
						(secondGroupNode = instance(1792,7))
						(active = "1")
					)
					SDUPluginClearance::ConnectionNodeClearance(
						(name = "Gripper <-> TableDifficult")
						(flags = "Show | Select")
						(firstGroupNode = instance(1789,1913,73))
						(secondGroupNode = instance(1792,8))
						(active = "1")
					)
				])
			)
			SDULibOMPL::SingleQuerySetupNode(
				(name = "OMPL")
				(flags = "Show | Select")
				(childNodes = [
					VSLibPoseList::PoseList(
						(name = "PoseList")
						(flags = "Select")
						(poses = [
							VSLibPoseList::Pose(
								(name = "Pose_0")
								(flags = "Show | Select")
								(relFrameTransform = 
									VSD3D::FrameTransform(
										(relFrame = "(-0.99968630141862624,-0.0012135489809111388,0.025016515641040387,-0.45939918114524275,-0.00058968352395638579,0.99968901406130994,0.024930452030953482,-0.43116297695832922,-0.025038990181096833,0.024907879556417996,-0.99937612864562353,0.038026990292783044,0,0,0,1)")
									)
								)
								(definition = 
									VSLibPoseList::JointPoseExtension(
										(jointValues = ["-2.4522898173129168" "-2.048487637906081" "-0.96117835487280923" "-1.7378911672315449" "1.5674682376489379" "-0.88233686072194895"])
									)
								)
								(associatedKinematic = instance(1789,1913,56))
							)
							VSLibPoseList::Pose(
								(name = "Pose_1")
								(flags = "Show | Select")
								(relFrameTransform = 
									VSD3D::FrameTransform(
										(relFrame = "(0.021569525822432736,0.074834304923280123,0.99696267852033715,0.063801879641980974,0.0027528554560568436,-0.99719534046933889,0.074792210377001234,-0.32955695215750341,0.99976356071955019,0.0011312616360063255,-0.021715038670871271,0.12577484984234361,0,0,0,1)")
									)
								)
								(definition = 
									VSLibPoseList::JointPoseExtension(
										(jointValues = ["-1.271446080113986" "-1.874783766380945" "-2.3201196007348099" "-2.185553166193293" "-2.9160917716875678" "1.4748413368848809"])
									)
								)
								(associatedKinematic = instance(1789,52))
							)
						])
						(posesRadius = "0.050000000000000003")
						(posesColor = "(84,171,255)")
						(isAutoCreated = "0")
					)
				])
				(robot = 
					SDULibOMPL::JointKinematicRobotInstance(
						(root = instance(1789,52))
					)
				)
				(start = 
					SDULibOMPL::StartPoseInstance(
						(start = 
							SDULibOMPL::JointPoseSourceInstance(
								(values = [6:"-2.4522898173129168" "-2.048487637906081" "-0.96117835487280923" "-1.7378911672315449" "1.5674682376489379" "-0.88233686072194895"])
							)
						)
					)
				)
				(goal = 
					SDULibOMPL::GoalPoseInstance(
						(goal = 
							SDULibOMPL::JointPoseSourceInstance(
								(values = [6:"-1.271446080113986" "-1.874783766380945" "-2.3201196007348099" "-2.185553166193293" "-2.9160917716875678" "1.4748413368848809"])
							)
						)
					)
				)
				(stateSpace = 
					SDULibOMPL::R6StateSpaceInstance(
					)
				)
				(boundaries = 
					SDULibOMPL::BoundaryInstance(
						(min = [6:"-3.1400000000000001" "-3.1400000000000001" "-3.1400000000000001" "-3.1400000000000001" "-3.1400000000000001" "-3.1400000000000001"])
						(max = [6:"3.1400000000000001" "3.1400000000000001" "3.1400000000000001" "3.1400000000000001" "3.1400000000000001" "3.1400000000000001"])
						(offset = [6:"0" "0" "0" "0" "0" "0"])
					)
				)
				(params = [
					SDULibOMPL::RangeParamInstance(
						(value = ".1")
					)
				])
				(planner = 
					SDULibOMPL::RRTConnectPlannerInstance(
						(id = "RRTConnect")
						(run = "1")
						(solveTime = "60")
						(simplify = "0")
						(simplifyTime = "60")
					)
				)
				(solutions = [
					SDULibOMPL::SolutionInstance(
						(name = "210728-225145: 1->1 (1)")
						(type = "Joint")
						(storage = [56:"(-2.4522898173129168,-2.048487637906081,-0.96117835487280923,-1.7378911672315449,1.5674682376489379,-0.88233686072194895)" "(-2.4168415017145333,-1.9779139878956269,-0.98927085591199637,-1.7301957095007732,1.5249488548519388,-0.91560050826215067)" "(-2.4038518268302185,-1.976744410976635,-1.0043637157134524,-1.7353598172028266,1.4745840002359061,-0.8884910386303172)" "(-2.3824856806657615,-1.9748206252295464,-1.0291892984497044,-1.7438540313347224,1.3917410611430103,-0.84389986173380405)" "(-2.3611195345013041,-1.972896839482458,-1.0540148811859567,-1.7523482454666179,1.3088981220501148,-0.79930868483729078)" "(-2.3397533883368471,-1.9709730537353694,-1.0788404639222087,-1.7608424595985137,1.226055182957219,-0.75471750794077763)" "(-2.3183872421723897,-1.9690492679882809,-1.1036660466584609,-1.7693366737304093,1.1432122438643233,-0.71012633104426448)" "(-2.2970210960079327,-1.9671254822411923,-1.1284916293947129,-1.777830887862305,1.0603693047714275,-0.66553515414775133)" "(-2.2756549498434753,-1.9652016964941039,-1.1533172121309652,-1.7863251019942008,0.97752636567853179,-0.62094397725123818)" "(-2.2542888036790183,-1.9632779107470153,-1.1781427948672172,-1.7948193161260964,0.89468342658563604,-0.57635280035472503)" "(-2.2329226575145609,-1.9613541249999269,-1.2029683776034692,-1.8033135302579919,0.81184048749274029,-0.53176162345821187)" "(-2.2115565113501039,-1.9594303392528383,-1.2277939603397212,-1.8118077443898877,0.72899754839984465,-0.48717044656169867)" "(-2.1901903651856465,-1.9575065535057499,-1.2526195430759732,-1.8203019585217834,0.6461546093069489,-0.44257926966518552)" "(-2.1688242190211895,-1.9555827677586612,-1.2774451258122252,-1.828796172653679,0.56331167021405315,-0.39798809276867236)" "(-2.1474580728567321,-1.9536589820115728,-1.3022707085484773,-1.8372903867855745,0.4804687311211574,-0.35339691587215921)" "(-2.1260919266922751,-1.9517351962644842,-1.3270962912847293,-1.8457846009174703,0.3976257920282617,-0.30880573897564606)" "(-2.1047257805278177,-1.9498114105173958,-1.3519218740209813,-1.8542788150493661,0.31478285293536601,-0.26421456207913291)" "(-2.0833596343633602,-1.9478876247703072,-1.3767474567572333,-1.8627730291812616,0.23193991384247026,-0.21962338518261976)" "(-2.0619934881989028,-1.9459638390232188,-1.4015730394934853,-1.8712672433131572,0.14909697474957456,-0.17503220828610661)" "(-2.0406273420344454,-1.9440400532761302,-1.4263986222297373,-1.879761457445053,0.066254035656678825,-0.13044103138959345)" "(-2.019261195869988,-1.9421162675290418,-1.4512242049659894,-1.8882556715769487,-0.016588903436216884,-0.085849854493080288)" "(-1.9978950497055308,-1.9401924817819531,-1.4760497877022414,-1.8967498857088443,-0.09943184252911258,-0.04125867759656713)" "(-1.9765289035410736,-1.9382686960348647,-1.5008753704384934,-1.9052440998407398,-0.18227478162200828,0.003332499299946029)" "(-1.9551627573766164,-1.9363449102877761,-1.5257009531747454,-1.9137383139726354,-0.26511772071490397,0.047923676196459188)" "(-1.9337966112121592,-1.9344211245406877,-1.5505265359109974,-1.9222325281045309,-0.34796065980779967,0.092514853092972346)" "(-1.912430465047702,-1.9324973387935991,-1.5753521186472494,-1.9307267422364265,-0.43080359890069536,0.13710602998948551)" "(-1.8910643188832448,-1.9305735530465107,-1.6001777013835015,-1.939220956368322,-0.51364653799359106,0.18169720688599866)" "(-1.8696981727187876,-1.9286497672994221,-1.6250032841197535,-1.9477151705002176,-0.59648947708648681,0.22628838378251181)" "(-1.8483320265543304,-1.9267259815523337,-1.6498288668560055,-1.9562093846321131,-0.67933241617938256,0.27087956067902497)" "(-1.8269658803898732,-1.924802195805245,-1.6746544495922575,-1.9647035987640087,-0.76217535527227831,0.31547073757553812)" "(-1.805599734225416,-1.9228784100581566,-1.6994800323285095,-1.9731978128959042,-0.84501829436517406,0.36006191447205127)" "(-1.7842335880609588,-1.920954624311068,-1.7243056150647615,-1.9816920270277998,-0.92786123345806981,0.40465309136856442)" "(-1.7628674418965016,-1.9190308385639796,-1.7491311978010136,-1.9901862411596953,-1.0107041725509656,0.44924426826507757)" "(-1.7415012957320444,-1.917107052816891,-1.7739567805372656,-1.9986804552915909,-1.0935471116438613,0.49383544516159072)" "(-1.7201351495675872,-1.9151832670698026,-1.7987823632735176,-2.0071746694234864,-1.1763900507367571,0.53842662205810388)" "(-1.69876900340313,-1.913259481322714,-1.8236079460097696,-2.015668883555382,-1.2592329898296528,0.58301779895461703)" "(-1.6774028572386728,-1.9113356955756255,-1.8484335287460216,-2.0241630976872775,-1.3420759289225486,0.62760897585113018)" "(-1.6560367110742156,-1.9094119098285369,-1.8732591114822736,-2.0326573118191731,-1.4249188680154443,0.67220015274764333)" "(-1.6346705649097584,-1.9074881240814485,-1.8980846942185257,-2.0411515259510686,-1.5077618071083401,0.71679132964415648)" "(-1.6133044187453012,-1.9055643383343599,-1.9229102769547777,-2.0496457400829642,-1.5906047462012358,0.76138250654066963)" "(-1.591938272580844,-1.9036405525872715,-1.9477358596910297,-2.0581399542148597,-1.6734476852941316,0.80597368343718279)" "(-1.5705721264163868,-1.9017167668401829,-1.9725614424272817,-2.0666341683467553,-1.7562906243870273,0.85056486033369594)" "(-1.5492059802519296,-1.8997929810930945,-1.9973870251635337,-2.0751283824786508,-1.8391335634799231,0.89515603723020909)" "(-1.5278398340874724,-1.8978691953460058,-2.0222126078997857,-2.0836225966105464,-1.9219765025728188,0.93974721412672224)" "(-1.5064736879230152,-1.8959454095989174,-2.0470381906360378,-2.0921168107424419,-2.0048194416657146,0.98433839102323539)" "(-1.485107541758558,-1.894021623851829,-2.0718637733722898,-2.1006110248743375,-2.0876623807586103,1.0289295679197485)" "(-1.4637413955941008,-1.8920978381047406,-2.0966893561085418,-2.109105239006233,-2.1705053198515061,1.0735207448162618)" "(-1.4423752494296436,-1.8901740523576522,-2.1215149388447938,-2.1175994531381286,-2.2533482589444018,1.1181119217127751)" "(-1.4210091032651864,-1.8882502666105638,-2.1463405215810458,-2.1260936672700241,-2.3361911980372976,1.1627030986092883)" "(-1.3996429571007292,-1.8863264808634754,-2.1711661043172978,-2.1345878814019197,-2.4190341371301933,1.2072942755058014)" "(-1.378276810936272,-1.884402695116387,-2.1959916870535499,-2.1430820955338152,-2.5018770762230891,1.2518854524023146)" "(-1.3569106647718148,-1.8824789093692986,-2.2208172697898019,-2.1515763096657108,-2.5847200153159848,1.2964766292988279)" "(-1.3355445186073576,-1.8805551236222102,-2.2456428525260539,-2.1600705237976063,-2.6675629544088806,1.3410678061953412)" "(-1.3141783724429004,-1.8786313378751218,-2.2704684352623059,-2.1685647379295019,-2.7504058935017763,1.3856589830918544)" "(-1.2928122262784432,-1.8767075521280334,-2.2952940179985579,-2.1770589520613974,-2.8332488325946721,1.4302501599883677)" "(-1.271446080113986,-1.874783766380945,-2.3201196007348099,-2.185553166193293,-2.9160917716875678,1.4748413368848809)"])
						(infos = [
							SDULibOMPL::SolutionInfoInstance(
								(name = "planTime [s]")
								(value = "7.98161")
							)
							SDULibOMPL::SolutionInfoInstance(
								(name = "simplifyTime [s]")
								(value = "1.1e-06")
							)
						])
						(status = "Exact solution")
					)
				])
			)
			VSD::Node(
				(name = "ServiceBlocks")
				(flags = "Show | Select")
			)
			VSD::Node(
				(name = "PoseLists")
				(flags = "Show | Select")
			)
			VSLibPoseList::PoseList(
				(name = "PoseList #3")
				(flags = "Show | Select")
				(poses = [
					VSLibPoseList::Pose(
						(myModelInstanceId = "1795")
						(name = "Pose_0")
						(flags = "Show | Select")
						(relFrameTransform = 
							VSD3D::FrameTransform(
								(relFrame = "(-0.99968630141862636,-0.0012135489809110833,0.025016515641042597,-0.064000000000000001,-0.00058968352395635804,0.99968901406130983,0.02493045203095438,-0.4356539397422331,-0.025038990181099022,0.02490787955641903,-0.99937612864562353,0.20201464985170775,0,0,0,1)")
							)
						)
						(definition = 
							VSLibPoseList::JointPoseExtension(
								(jointValues = ["-1.4158771252965243" "-1.6871707082833929" "-2.2531564920358029" "-0.79284358469263383" "1.5993639056680076" "0.15372042999615726"])
							)
						)
						(associatedKinematic = instance(1789,52))
					)
				])
				(posesRadius = "0.050000000000000003")
				(posesColor = "(84,171,255)")
				(isAutoCreated = "0")
			)
		])
	)
)
