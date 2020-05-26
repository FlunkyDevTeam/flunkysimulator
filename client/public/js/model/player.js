

export  function generateSpectatorHTML(player) {
    return generatePlayerHTML(player, throwingPlayer = false, isOwnTeam = false, hasStrafbier = false, isSpectator = true);
}

export function generatePlayerHTML(player, throwingPlayer = false, isOwnTeam = false, hasStrafbier = false, isSpectator = false) {
    name = player.name;
    isHimself = name === playerName;
    turnClass = name === throwingPlayer ? ' btn-primary' : ' btn-default';
    egoClass = isHimself ? ' egoplayer' : '';
    hasAbgegebenClass = player.abgegeben ? ' disabled' : '';

    // disabled for own team and not abgegeben
    mayValidateAbgabeClass = !isOwnTeam ? "" : " disabled";
    // TODO discussion: hasStrafbier && isHimself ? "" : "disabled";
    mayRejoinClass = ""

    playerSpan = name === playerName
        ? $('<span>')
            .append($('<span class="glyphicon glyphicon-chevron-right smaller-font">'))
            .append(name)
            .append($('<span class="glyphicon glyphicon-chevron-left smaller-font">'))
        : name;
    playerbutton = $("<a href='#'>").addClass("btn namebutton" + turnClass + egoClass + hasAbgegebenClass).html(playerSpan)
    if (!isSpectator) {
        playerbutton
            .click(((n) => () => selectThrowingPlayer(n))(name))
            .attr({
                "data-toggle": "tooltip",
                "title": "Werfer machen"
            });
    }

    html = $('<div role="group">').addClass("btn-group btn-group-justified vspace-small playerbuttongroup")
        .append(playerbutton)
        .append($('<div role="group">').addClass("btn-group")
            .append($("<a href='#'>").addClass("btn btn-default dropdown-toggle").attr({
                "type": "button",
                "data-toggle": "dropdown",
                "data-toggle-second": "tooltip",
                "aria-haspopup": "true",
                "aria-expanded": "false",
                "title": "Spieler verschieben",
            }).append($("<span>").addClass("glyphicon glyphicon-transfer")))
            .append($("<ul>").addClass("dropdown-menu")
                .append($("<li>")
                    .append($("<a href='#'>").addClass("switchteamabutton").text("Linkes Team"))
                    .click(((n) => () => switchTeam(EnumTeams.TEAM_A_TEAMS, n))(name)))
                .append($("<li>")
                    .append($("<a href='#'>").addClass("switchteambbutton").text("Rechtes Team"))
                    .click(((n) => () => switchTeam(EnumTeams.TEAM_B_TEAMS, n))(name)))
                .append($("<li>")
                    .append($("<a href='#'>").addClass("switchspectatorbutton").text("Zuschauer"))
                    .click(((n) => () => switchTeam(EnumTeams.SPECTATOR_TEAMS, n))(name)))));
    // Abgabe / TakeStrafbier button
    if (!isSpectator) {
        if (player.abgegeben) {
            html.append($("<a href='#' data-toggle='tooltip' title='Strafbier übernehmen'>")
                .addClass("btn btn-default abgebenbutton" + mayRejoinClass)
                .click(((n) => function () {
                    toggleAbgabe(n);
                    // TODO needs intelligent button hiding!
                    // reduceStrafbierCount(EnumTeams.TEAM_A_TEAMS);
                })(name, player.abgegeben))
                .append($("<span>").addClass("glyphicon glyphicon-refresh"))
            );
        } else {
            html.append($("<a href='#' data-toggle='tooltip' title='Abgabe abnehmen'>")
                .addClass("btn btn-default abgebenbutton" + mayValidateAbgabeClass)
                .click(((n) => () => toggleAbgabe(n))(name))
                .append($("<span>").addClass("glyphicon glyphicon-ok-circle"))
            );
        }
    }

    html.append($("<a href='#' data-toggle='tooltip' title='Spieler kicken'>")
        .addClass("btn btn-default kickbutton")
        .click(((n) => function () {
            if (confirm(`Möchtest du "${n}" wirklich kicken?`)) {
                kickPlayer(n);
            }
        })(name))
        .append($("<span>").addClass("glyphicon glyphicon-ban-circle"))
    );

    return html;
}
