mkdir aow\acs
bcc aow/src/aow.acs aow/acs/aow.o
@if ERRORLEVEL 1 (
	echo BCC FAILED
	PAUSE
	EXIT
)

py tools/acsinclude.py aow/src/aow.acs aow/src/aowmap.acs
@if ERRORLEVEL 1 (
	echo ACSINCLUDE FAILED
	PAUSE
	EXIT
)

py tools/sndinfogen.py aow
@if ERRORLEVEL 1 (
	echo SNDINFOGEN FAILED
	PAUSE
	EXIT
)
