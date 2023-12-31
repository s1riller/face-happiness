import Vuex from 'vuex';
import typeFace from "@/store/modules/typeFace"; // Импортируйте Vue
import Signup from "@/store/modules/Signup";
import ProfileModule from "@/store/modules/ProfileModule"
import GetData from "@/store/modules/GetData"
import FetchUserResults from "@/store/modules/FetchUserResults";
import FetchMedicines from "@/store/modules/FetchMedicines";
export default  new Vuex.Store({
    modules:{Signup,ProfileModule,GetData,FetchUserResults,FetchMedicines}
});
