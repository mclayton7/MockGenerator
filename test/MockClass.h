#pragma once

#include <I_SimpleInterface.h>
#include <QObject>
#include <gtest/gmock.h>

class MockSimpleInterface : public QObject, public I_SimpleInterface
{
    Q_OBJECT

public:
    explicit MockSimpleInterface();
    virtual ~MockSimpleInterface();

    MOCK_CONST_METHOD0(voidMethodConst, void());
    MOCK_METHOD0(voidMethod, void());
    MOCK_CONST_METHOD0(qStringMethodConst, QString());
    MOCK_METHOD0(qStringMethod, QString());
    MOCK_CONST_METHOD0(constQStringRefMethodConst, const QString &());
    MOCK_METHOD0(constQStringRefMethod, const QString &());
    MOCK_CONST_METHOD0(qStringRefMethodConst, QString &());
    MOCK_METHOD0(qStringRefMethod, QString &());
    MOCK_METHOD1(voidOneIntArgMethod, void(int count));
    MOCK_CONST_METHOD1(voidOneIntArgMethodConst, void(int count));
    MOCK_METHOD1(voidOneRefArgMethod, void(QString & stringArg));
    MOCK_CONST_METHOD1(voidOneRefArgMethodConst, void(QString & stringArg));
    MOCK_METHOD1(voidOneConstRefArgMethod, void(const QString & stringArg));
    MOCK_CONST_METHOD1(voidOneConstRefArgMethodConst, void(const QString & stringArg));
    MOCK_METHOD0(protectedButNotASignal, void());

    void emitSimpleSignal();
    void emitSignalWithOneIntArg(int value0);
    void emitSignalWithTwoIntArgs(int value0, int value1);
    void emitSignalWithOneRefArg(const QString & value0);
    
signals:
    void simpleSignal();
    void signalWithOneIntArg(int count);
    void signalWithTwoIntArgs(int countint );
    void signalWithOneRefArg(const QString & stringArg);

};
