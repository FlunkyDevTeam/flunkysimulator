package simulator.control

import de.flunkyteam.endpoints.projects.simulator.EnumLoginStatus
import de.flunkyteam.endpoints.projects.simulator.EnumTeams
import io.mockk.mockk
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test
import simulator.model.game.Team

internal class PlayerControllerTest{

    @Test
    fun dryRun(){
        val messageController = mockk<MessageController>()
        val videoController = mockk<VideoController>()
        val clientManager = mockk<ClientManager>()
        val gameController = GameController(videoController, messageController,clientManager)

        val playerController = gameController.playerController

        val res1 =  playerController.registerPlayer("hans",null)
        assertEquals(PlayerController.LoginResp(EnumLoginStatus.LOGIN_STATUS_SUCCESS,"hans"),
            res1)

        val res2 = playerController.registerPlayer("hans",null)
        assertEquals(PlayerController.LoginResp(EnumLoginStatus.LOGIN_STATUS_NAME_TAKEN,"hans"),
            res2)

        playerController.registerPlayer("lola",null)
        playerController.registerPlayer("peter",null)
        playerController.registerPlayer("anna",null)

        val hans = playerController.getPlayer("hans")
        assertNotNull(hans)
        val lola = playerController.getPlayer("lola")
        assertNotNull(lola)
        val peter = playerController.getPlayer("peter")
        assertNotNull(peter)
        val anna = playerController.getPlayer("anna")
        assertNotNull(anna)

        assertEquals(4,playerController.Spectators.size)

        playerController.setPlayerTeam("hans", EnumTeams.TEAM_A_TEAMS)
        playerController.setPlayerTeam("lola", EnumTeams.TEAM_A_TEAMS)
        playerController.setPlayerTeam("peter", EnumTeams.TEAM_B_TEAMS)
        playerController.setPlayerTeam("anna", EnumTeams.TEAM_B_TEAMS)

        assertEquals(2,playerController.TeamA.size)
        assertEquals(2,playerController.TeamB.size)

        playerController.removePlayer("anna")
        assertEquals(1,playerController.TeamB.size)

        playerController.registerTeamWin(Team.A)
        assertEquals(1, hans!!.wonGames)
        assertEquals(1, lola!!.wonGames)
        assertEquals(0, peter!!.wonGames)
    }
}